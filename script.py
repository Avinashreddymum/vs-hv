#!/usr/bin/python

import csv

import MySQLdb as mdb
from config import defaults
import config

if __name__ == '__main__':
    pass
# print(defaults.dbURL)


def read_csv_chasis(path):
    rows = []
    with open(path, "r") as f_obj:
        reader = csv.reader(f_obj, delimiter='|',)
        for line in reader:
            try:
                if((line[1].strip() == "zone" or line[1].strip() == "")and len(line) < 18):
                    continue

                # if len(line) >= 17: # NFS cluster removing
                #     line = line[:2]+line[3:]

                rows.append([lin.strip() for lin in line[1:-1]])

            except Exception as e:
                # print("wrong format for line")
                # print(e)
                pass

    return rows


def split_brace(strs):
    one = strs[:strs.index('(')]
    two = strs[strs.index('(') + 1:strs.index(')')]
    return one, two


def get_clean_chasis_tuple(source_row):
    temp_list = []
    for i, val in enumerate(source_row):

        if i == 0:
            temp_list.append(val[len(val) - 1])
            continue
        elif i == 1:
            temp_list.append(get_cluster_id(val))
            continue
        elif i == 4 :
            temp_list.append(config.get_flavor(val))
            continue
        elif i == 8 or i == 12:
            temp_list += list(split_brace(val))
            continue
        elif i == 14:
            temp_list.append(get_cluster_id(val))
            continue
        else:
            temp_list.append(val)

    return tuple(temp_list)


# converts 000001 to 1
def get_cluster_id(val):
    return str(int(val))


def create_and_populate(rows):

    con = mdb.connect(host=defaults.host, user=defaults.username, passwd=defaults.password, db=defaults.database)

    with con:
        cur = con.cursor()

        for row in rows:
            try:
                tuple_conv = get_clean_chasis_tuple(row)
                cur.execute(config.get_daily_insert_query(row[3]), tuple_conv)
            except Exception as e:
                print("row is not inserted" + str(row) + str(tuple_conv))
                print(e)


rows = read_csv_chasis('vs-hv.csv')
create_and_populate(rows)
