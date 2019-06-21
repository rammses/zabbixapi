import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MonitoringIntegration.settings')

import django

django.setup()

# from zabbix.base import *
# aa = ZabbixClient4_1()
# aa.list_host_alarms('65198')



from zabbix.models import Machines

id_= 8
m = Machines.objects.get(id=int(id_))
print(m.name)