import mysql.connector
from MonitoringIntegration import settings as settings
from zabbix.zabbix.base import Base


class SetupZabbix():
    hostname=settings.Machines_db_hostname
    database=settings.Machines_db_database
    user = settings.Machines_db_user
    password = settings.Machines_db_password

    def deduplicate_by_ip(self, a):
        """
        Clears Empty ip address records from list
        removes duplicates by
        :param a:
        :return:
        """

        source_ips = []
        new_list = []
        for i in range(len(a)):
            if a[i][0] != None:
                if a[i][0] not in source_ips:
                    source_ips.append(a[i][0])
                    new_list.append(a[i])
        return new_list

    def get_machines_from_sql(self):
        try:
            connection = mysql.connector.connect(host=self.hostname,
                                                 database=self.database,
                                                 user=self.user,
                                                 password=self.password)
            machines_to_add = []
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute("select * from machines")
                record = cursor.fetchall()
                count = len(record)

                for n in range(count):
                    # print('step ', n, 'Machine Name :', record[n][1], 'Machine Address :', record[n][4])
                    # machines_to_add.append(record[n][4])
                    record1 = [record[n][4], record[n][1]]
                    machines_to_add.append(record1)

        except ConnectionError as e:
            print("Error while connecting to MySQL", e)
        finally:
            # closing database connection.
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                # de-duplication and cleaning of no address machines_to_add
                source_ips = []
                new_list = []
                for i in range(len(machines_to_add)):
                    if machines_to_add[i][0] != None:
                        if machines_to_add[i][0] not in source_ips:
                            source_ips.append(machines_to_add[i][0])
                            new_list.append(machines_to_add[i])
                return new_list

    def check_existence(self, address):
        payload = {
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                "filter": {
                    "host": [
                        address
                    ]
                }
            },
            "auth": Base.authenticate(),
            "id": 1
        }
        response_result = Base.Do_Request(payload)
        if response_result == []:
            exists = False
            return exists
        else:
            exists = True
            return exists


    def add_host_snmp(self, hosts_to_add):
        counter = 0

        for i in range(len(hosts_to_add)):
            if self.check_existence(hosts_to_add[i][0]) == False:
                print()
                payload = {
                        "jsonrpc": "2.0",
                        "method": "host.create",
                        "params": {
                            "host": hosts_to_add[i][0],
                            "interfaces": [
                                {
                                    "type": 2,
                                    "main": 1,
                                    "useip": 1,
                                    "ip": hosts_to_add[i][0],
                                    "dns": "",
                                    "port": "161"
                                }
                            ],
                            "groups": [
                                {
                                    "groupid": "29"
                                }
                            ],
                            "tags": [
                                {
                                    "tag": "Added by",
                                    "value": "Zabbix api"
                                },
                                {
                                    "tag": "Owner",
                                    "value": "Mobilenoc.mobi"
                                }
                            ],
                            "templates": [
                                {
                                    "templateid": "10226"
                                }
                            ],
                            "macros": [
                                {
                                    "macro": "{$SNMP_COMMUNITY}",
                                    "value": "Spr1ngf13ld"
                                }
                            ],
                            "name": 'Delete_Me_'+hosts_to_add[i][1],
                            "inventory_mode": 0,
                            "inventory": {
                                "macaddress_a": "01234",
                                "macaddress_b": "56768"
                            }
                        },
                        "auth": Base.authenticate(),
                        "id": 1
                    }
                print('Adding host :', hosts_to_add[i][0])
                print(payload)
                Base.Do_Request(payload)
                print('Hosts added :', hosts_to_add[i][0])
            else:
                print('host found skipping :', hosts_to_add[i][0])
            counter += 1
        response = 'all hosts added', counter
        return response



