from zabbix.zabbix.base import Base
from zabbix.zabbix.utils import SetupZabbix


def initialize_zabbix():
    try:
        token = Base.authenticate()
        # print(token)
        zabbix_stuff = SetupZabbix()
        machine_list = zabbix_stuff.get_machines_from_sql()
        zabbix_stuff.add_host_snmp(machine_list)
        success = True
        return success
    except:
        print('error occured :')
        success = False
        return success




