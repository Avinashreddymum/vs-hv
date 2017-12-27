class defaults:
    host = 'localhost'
    username = 'root'
    password = 'redhat'
    database = 'vs_hv'

    # queries #

    daily_insert_query = "INSERT INTO `{}_daily` (`timestamp`, `group_name`, `clusterID`, `os_type`, `hostname`, `island`, `reserved`, " + \
        "`status`, `state`, `vcpus`, `vcpus_os`, `vcpu_used`, `vram`, `vram_used`, `memory`, `memory_used`, `run_vms`) VALUES " + \
        "(CURDATE(), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    kw1_daily_insert_query = "INSERT INTO `kw1_daily` (`timestamp`, `group_name`, `clusterID`, `os_type`, `hostname`, `island`, `reserved`, " + \
        "`status`, `state`, `vcpus`, `vcpus_os`, `vcpu_used`, `vram`, `vram_used`, `memory`, `memory_used`, `run_vms`, `NFScluster`) VALUES " + \
        "(CURDATE(), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"


    realtime_insert_query = "INSERT INTO `{}_realtime` (`group_name`, `clusterID`, `os_type`, `hostname`, `island`, `reserved`, " + \
        "`status`, `state`, `vcpus`, `vcpus_os`, `vcpu_used`, `vram`, `vram_used`, `memory`, `memory_used`, `run_vms`) VALUES " + \
        "( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    kw1_realtime_insert_query = "INSERT INTO `kw1_realtime` (`group_name`, `clusterID`, `os_type`, `hostname`, `island`, `reserved`, " + \
        "`status`, `state`, `vcpus`, `vcpus_os`, `vcpu_used`, `vram`, `vram_used`, `memory`, `memory_used`, `run_vms`, `NFScluster`) VALUES " + \
        "( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    realtime_truncate_query = "TRUNCATE {}_realtime"

    create_table_daily = "CREATE TABLE `vs-hv`.`{}_daily` ( " + \
        "`timestamp` DATE NOT NULL, `group_name` VARCHAR(1) NOT NULL , `clusterID` INT NOT NULL , " + \
        "`os_type` VARCHAR(8) NOT NULL , `hostname` VARCHAR(20) NOT NULL , `island` VARCHAR(20) NOT NULL , " + \
        "`reserved` VARCHAR(20) NOT NULL , `status` VARCHAR(20) NOT NULL , `state` VARCHAR(20) NOT NULL , " + \
        "`vcpus` INT NOT NULL , `vcpus_os` INT NOT NULL , `vcpu_used` INT NOT NULL , `vram` INT NOT NULL , " + \
        "`vram_used` INT NOT NULL , `memory` INT NOT NULL , `memory_used` INT NOT NULL , `run_vms` INT NOT NULL ) " + \
        "ENGINE = InnoDB COMMENT = 'realtime chasis table'"

    kw1_create_table_daily = "CREATE TABLE `vs-hv`.`kw1_daily` ( " + \
        "`timestamp` DATE NOT NULL, `group_name` VARCHAR(1) NOT NULL , `clusterID` INT NOT NULL , " + \
        "`os_type` VARCHAR(8) NOT NULL , `hostname` VARCHAR(20) NOT NULL , `island` VARCHAR(20) NOT NULL , " + \
        "`reserved` VARCHAR(20) NOT NULL , `status` VARCHAR(20) NOT NULL , `state` VARCHAR(20) NOT NULL , " + \
        "`vcpus` INT NOT NULL , `vcpus_os` INT NOT NULL , `vcpu_used` INT NOT NULL , `vram` INT NOT NULL , " + \
        "`vram_used` INT NOT NULL , `memory` INT NOT NULL , `memory_used` INT NOT NULL , `run_vms` INT NOT NULL ,`NFScluster` INT NOT NULL) " + \
        "ENGINE = InnoDB COMMENT = 'realtime chasis table'"

    create_table_realtime = "CREATE TABLE `vs-hv`.`{}_realtime` ( " + \
        "`group_name` VARCHAR(1) NOT NULL , `clusterID` INT NOT NULL , " + \
        "`os_type` VARCHAR(8) NOT NULL , `hostname` VARCHAR(20) NOT NULL , `island` VARCHAR(20) NOT NULL , " + \
        "`reserved` VARCHAR(20) NOT NULL , `status` VARCHAR(20) NOT NULL , `state` VARCHAR(20) NOT NULL , " + \
        "`vcpus` INT NOT NULL , `vcpus_os` INT NOT NULL , `vcpu_used` INT NOT NULL , `vram` INT NOT NULL , " + \
        "`vram_used` INT NOT NULL , `memory` INT NOT NULL , `memory_used` INT NOT NULL , `run_vms` INT NOT NULL ) " + \
        "ENGINE = InnoDB COMMENT = 'realtime chasis table'"

    kw1_create_table_realtime = "CREATE TABLE `vs-hv`.`kw1_realtime` ( " + \
        "`group_name` VARCHAR(1) NOT NULL , `clusterID` INT NOT NULL , " + \
        "`os_type` VARCHAR(8) NOT NULL , `hostname` VARCHAR(20) NOT NULL , `island` VARCHAR(20) NOT NULL , " + \
        "`reserved` VARCHAR(20) NOT NULL , `status` VARCHAR(20) NOT NULL , `state` VARCHAR(20) NOT NULL , " + \
        "`vcpus` INT NOT NULL , `vcpus_os` INT NOT NULL , `vcpu_used` INT NOT NULL , `vram` INT NOT NULL , " + \
        "`vram_used` INT NOT NULL , `memory` INT NOT NULL , `memory_used` INT NOT NULL , `run_vms` INT NOT NULL ,`NFScluster` INT NOT NULL) " + \
        "ENGINE = InnoDB COMMENT = 'realtime chasis table'"

    #slack tables

    realtime_slack_truncate_query = "TRUNCATE {}_slack_realtime"

    slack_create_table_daily = "CREATE TABLE `vs-hv`.`{}_slack_daily` ( " + \
        "`timestamp` DATE NOT NULL, `menu` VARCHAR(20) NOT NULL, `group_name` VARCHAR(10) NOT NULL , `hostname` VARCHAR(20) NOT NULL ," + \
        "`status` VARCHAR(20) NOT NULL , `SVMs_available` VARCHAR(20) NOT NULL , " + \
        "`SVMs_provisioned` DOUBLE NOT NULL , `capacity_physical` DOUBLE NOT NULL, " + \
        "`capacity_available` DOUBLE NOT NULL , `IOPS_available` DOUBLE NOT NULL, "  + \
        "`LUNsize_provisioned` DOUBLE NOT NULL , `IOPS_provisioned` DOUBLE NOT NULL ) " + \
        " ENGINE = InnoDB COMMENT = 'daily slack chasis table'; "

    slack_create_table_realtime = "CREATE TABLE `vs-hv`.`{}_slack_realtime` ( " + \
        "`menu` VARCHAR(20) NOT NULL, `group_name` VARCHAR(10) NOT NULL , `hostname` VARCHAR(20) NOT NULL ," + \
        "`status` VARCHAR(20) NOT NULL , `SVMs_available` VARCHAR(20) NOT NULL , " + \
        "`SVMs_provisioned` DOUBLE NOT NULL , `capacity_physical` DOUBLE NOT NULL, " + \
        "`capacity_available` DOUBLE NOT NULL , `IOPS_available` DOUBLE NOT NULL, "  + \
        "`LUNsize_provisioned` DOUBLE NOT NULL , `IOPS_provisioned` DOUBLE NOT NULL ) " + \
        " ENGINE = InnoDB COMMENT = 'daily slack chasis table'; "

    daily_slack_insert_query = "INSERT INTO `{}_slack_daily` (`timestamp`, `menu`, `group_name`, `hostname`, `status`," + \
         "`SVMs_available`, `SVMs_provisioned`, `capacity_physical`, `capacity_available`, `IOPS_available`," + \
         "`LUNsize_provisioned`, `IOPS_provisioned`) VALUES (CURDATE(), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "

    realtime_slack_insert_query = "INSERT INTO `{}_slack_realtime` (`menu`, `group_name`, `hostname`, `status`," + \
         "`SVMs_available`, `SVMs_provisioned`, `capacity_physical`, `capacity_available`, `IOPS_available`," + \
         "`LUNsize_provisioned`, `IOPS_provisioned`) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "




_flavour_dict = { "oracle-se2" : 'oracle-se2',
                 "oracle-se2-windows" : 'oracle-se2',
                 "oracle-se2-rhel" : 'oracle-se2',
                 "oracle-ee2" : 'oracle-ee2',
                 "oracle-ee2-windows" : 'oracle-ee2',
                 "oracle-ee2-rhel" : 'oracle-ee2',
                 }

'''
removes content (...) and checks
if conversion present in dict and send converted else send cleaned content

'''
def get_flavor(string):
    try:
        if string.__contains__('('):
            string = string[:string.index('(')]

        value = _flavour_dict[string.lower()]
        if not value == '':
            return value
    except Exception as e:
        # print(e)
        pass

    return string


def get_query(hostname, kw_query, default_query):
    try:
        query = ''
        loc = hostname.lower()[:3]
        if (loc == 'kw1'):
            query = kw_query
        elif (loc == 'hh3' or loc == 'lo8'):
            query = default_query.format("hh3")
        else:
            query = default_query.format(loc)
    except Exception as e:
        # print(e)
        pass

    return query


def get_realtime_truncate_query(hostname):
    return get_query(hostname, defaults.realtime_truncate_query.format("kw1"), defaults.realtime_truncate_query)


def get_daily_insert_query(hostname):
    return get_query(hostname, defaults.kw1_daily_insert_query, defaults.daily_insert_query)


def get_realtime_insert_query(hostname):
    return get_query(hostname, defaults.kw1_realtime_insert_query, defaults.realtime_insert_query)



def get_realtime_slack_truncate_query(hostname):
    return get_query(hostname, defaults.realtime_slack_truncate_query.format("kw1"), defaults.realtime_slack_truncate_query)


def get_daily_slack_insert_query(hostname):
    return get_query(hostname, defaults.daily_slack_insert_query.format("kw1"), defaults.daily_slack_insert_query)


def get_realtime_slack_insert_query(hostname):
    return get_query(hostname, defaults.realtime_slack_insert_query.format("kw1"), defaults.realtime_slack_insert_query)

