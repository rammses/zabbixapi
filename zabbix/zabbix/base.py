import requests
import json
import sys
from MonitoringIntegration import settings
#from rest_framework import viewsets, response, status

class Base():

    hostname = '142.93.198.151'
    database = 'dev'
    user = 'root'
    password = 'Mrk_9626'

    def Do_Request(pay_load):
        r = requests.post(settings.ZABBIX_SERVERURL, data=json.dumps(pay_load), headers=settings.ZABBIX_HEADERS)
        r = r.json()
        return r['result']

    @staticmethod
    def authenticate():
        payload = {"jsonrpc": "2.0",
                   "method": "user.login",
                   "params": {
                       "user": settings.ZABBIX_USERNAME,
                       "password": settings.ZABBIX_PASSWORD
                   },
                   "id": 1,
                   "auth": None}
        try:
            response_result = Base.Do_Request(payload)
            return response_result
        except requests.exceptions.RequestException as err:
            print('Connection Error occured', err)
            sys.exit(1)
        except KeyError as err:
            print("User password error please check", err)
            sys.exit(1)

    def ParseHostGroupId(group_name):
        payload = {
            "jsonrpc": "2.0",
            "method": "hostgroup.get",
            "params": {
                "output": "extend",
                "filter": {
                    "name": [
                        group_name
                    ]
                }
            },
            "auth": Base.authenticate(),
            "id": 1
        }
        R = requests.post(settings.ZABBIX_SERVERURL, data=json.dumps(payload), headers=settings.ZABBIX_HEADERS)
        R = R.json()
        raw_data = R['result']
        grpid = json.loads(json.dumps(raw_data[0]))
        return grpid['groupid']
