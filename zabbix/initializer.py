
from utils import get_machines
from zabbix.base import ZabbixClient4_1,ZabbixClientError


def initialize_zabbix():

    zabbix_client = ZabbixClient4_1()
    machines = get_machines()

    for host in machines:
        try:
            zabbix_client.add_machine(host.name, host.ip_address)
        except ZabbixClientError as err:
            print("failed to add machine = %r" % host.name)
