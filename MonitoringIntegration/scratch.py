import json


class HostsIds:

    def get_hostid_from_names(self, list1, name):

        for member in list1:
            feed_json = json.dumps((member))
            jsonized_list = json.loads(feed_json)

            if jsonized_list['host'] == name:
                hostid = jsonized_list['hostid']
                return hostid

    def get_name_from_hostids(self, list1 ,hostid):

        for member in list1:
            feed_json = json.dumps((member))
            jsonized_list = json.loads(feed_json)

            if jsonized_list['hostid'] == hostid:
                name = jsonized_list['host']
                return name


name = "mobilenoc-fw.mobilenoc.us"
hostid = "10264"
hosts = [
    {
        "hostid": "10084",
        "host": "Zabbix server"
    },
    {
        "hostid": "10264",
        "host": "mobilenoc-fw.mobilenoc.us"
    },
    {
        "hostid": "10265",
        "host": "N9396A"
    },
    {
        "hostid": "10266",
        "host": "NJSBCRSW1.mobilenoc.local"
    },
    {
        "hostid": "10267",
        "host": "mnoc-7Ka"
    },
    {
        "hostid": "10268",
        "host": "mobile-noc5K1"
    },
    {
        "hostid": "10269",
        "host": "F5-1"
    },
    {
        "hostid": "10270",
        "host": "F5-2"
    },
    {
        "hostid": "10271",
        "host": "Cloud"
    },
    {
        "hostid": "10272",
        "host": "4948_SW1"
    },
    {
        "hostid": "10273",
        "host": "DMZ_SWITCH"
    },
    {
        "hostid": "10274",
        "host": "WANART3845"
    },
    {
        "hostid": "10275",
        "host": "WANART3945"
    },
    {
        "hostid": "10276",
        "host": "asa-5515-fw"
    },
    {
        "hostid": "10277",
        "host": "N9396B"
    },
    {
        "hostid": "10278",
        "host": "mobilenoc5k1"
    },
    {
        "hostid": "10279",
        "host": "Arbor"
    },
    {
        "hostid": "10280",
        "host": "asa-5506-fw"
    },
    {
        "hostid": "10281",
        "host": "border1"
    },
    {
        "hostid": "10282",
        "host": "border2"
    },
    {
        "hostid": "10283",
        "host": "Fortinet1"
    },
    {
        "hostid": "10284",
        "host": "Non_VSS6500"
    },
    {
        "hostid": "10285",
        "host": "NexusLA"
    },
    {
        "hostid": "10286",
        "host": "mnoc-5k2"
    },
    {
        "hostid": "10287",
        "host": "Fortinet2"
    },
    {
        "hostid": "10288",
        "host": "6504NONVSS_SW1"
    },
    {
        "hostid": "10289",
        "host": "Opengear1"
    },
    {
        "hostid": "10290",
        "host": "asa_5510LA"
    },
    {
        "hostid": "10291",
        "host": "arista-sw1"
    },
    {
        "hostid": "10292",
        "host": "3560-"
    },
    {
        "hostid": "10293",
        "host": "arista-sw2"
    },
    {
        "hostid": "10294",
        "host": "3560"
    },
    {
        "hostid": "10295",
        "host": "netscaler1"
    },
    {
        "hostid": "10296",
        "host": "netscaler2"
    },
    {
        "hostid": "10297",
        "host": "Palo Alto"
    },
    {
        "hostid": "10298",
        "host": "Arbor CP"
    },
    {
        "hostid": "10299",
        "host": "fw-la5515"
    },
    {
        "hostid": "10300",
        "host": "fw-la2-5515"
    },
    {
        "hostid": "10301",
        "host": "NexusLA2"
    },
    {
        "hostid": "10302",
        "host": "ASALA5510"
    },
    {
        "hostid": "10303",
        "host": "asa-5506-fw2"
    },
    {
        "hostid": "10304",
        "host": "4948_SW2"
    },
    {
        "hostid": "10305",
        "host": "1.1.1.1"
    }
]

interfaces = [
    {
        "interfaceid": "1",
        "hostid": "10084",
        "main": "1",
        "type": "1",
        "useip": "1",
        "ip": "127.0.0.1",
        "dns": "",
        "port": "10050",
        "bulk": "1"
    },
    {
        "interfaceid": "4",
        "hostid": "10264",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "4.71.144.116",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "5",
        "hostid": "10265",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "4.71.144.101",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "6",
        "hostid": "10266",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "4.71.144.98",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "7",
        "hostid": "10267",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "4.30.132.65",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "8",
        "hostid": "10268",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "4.71.144.103",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "9",
        "hostid": "10269",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "4.30.132.82",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "10",
        "hostid": "10270",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "4.30.132.83",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "11",
        "hostid": "10271",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "166.151.129.129",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "12",
        "hostid": "10272",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "4.71.144.105",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "13",
        "hostid": "10273",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "4.71.144.111",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "14",
        "hostid": "10274",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "4.30.132.70",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "15",
        "hostid": "10275",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "4.30.132.71",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "16",
        "hostid": "10276",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "94.249.83.145",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "17",
        "hostid": "10277",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "4.71.144.102",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "18",
        "hostid": "10278",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "10.10.100.26",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "19",
        "hostid": "10279",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "4.30.132.92",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "20",
        "hostid": "10280",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "4.71.144.119",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "21",
        "hostid": "10281",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "4.71.144.96",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "22",
        "hostid": "10282",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "4.71.144.97",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "23",
        "hostid": "10283",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "4.71.144.123",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "24",
        "hostid": "10284",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "4.71.144.99",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "25",
        "hostid": "10285",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "162.221.4.98",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "26",
        "hostid": "10286",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "4.71.144.104",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "27",
        "hostid": "10287",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "4.71.144.124",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "28",
        "hostid": "10288",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "4.71.144.100",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "29",
        "hostid": "10289",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "166.151.129.130",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "30",
        "hostid": "10290",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "162.221.4.102",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "31",
        "hostid": "10291",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "166.151.129.129",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "32",
        "hostid": "10292",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "166.151.129.129",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "33",
        "hostid": "10293",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "166.151.129.130",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "34",
        "hostid": "10294",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "166.151.129.130",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "35",
        "hostid": "10295",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "166.151.18.23",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "36",
        "hostid": "10296",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "166.151.18.23",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "37",
        "hostid": "10297",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "166.151.18.23",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "38",
        "hostid": "10298",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "166.151.18.23",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "39",
        "hostid": "10299",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "162.221.4.100",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "40",
        "hostid": "10300",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "162.221.4.101",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "41",
        "hostid": "10301",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "162.221.4.99",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "42",
        "hostid": "10302",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "162.221.4.103",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "43",
        "hostid": "10303",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "4.71.144.120",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "44",
        "hostid": "10304",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "4.71.144.106",
        "dns": "",
        "port": "161",
        "bulk": "1"
    },
    {
        "interfaceid": "45",
        "hostid": "10305",
        "main": "1",
        "type": "2",
        "useip": "1",
        "ip": "1.1.1.1",
        "dns": "",
        "port": "161",
        "bulk": "1"
    }
]

test1 = HostsIds()
test2 = HostsIds()
print(test1.get_hostid_from_names(hosts, name))
print(test1.get_name_from_hostids(hosts, hostid))
