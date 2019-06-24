import os
from zabbix.base import ZabbixClient4_1 as ZabbixClient
from rest_framework import viewsets, response, status
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MonitoringIntegration.settings')

import django

django.setup()
from utils import check_for_special_chars_in_name as check_chars

from zabbix.base import *
from zabbix.utils import *
# aa = ZabbixClient4_1()
# aa.list_host_alarms('65198')


def get_cpu_history(id, itemid):
    params = {
        "output": "extend",
        "hostids": id,
        "history": 3,
        "itemids": itemid,
        "sortfield": "clock",
        "sortorder": "DESC",
        "limit": 2880
    }
    request = ZabbixClient._build_request('history.get', params=params)
    response_result = ZabbixClient.do_request(request)
    return response_result

print(get_cpu_history("10392","37982"))