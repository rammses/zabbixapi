import requests
import json
from MonitoringIntegration import settings
from utils import check_for_special_chars_in_name as check_chars

class ZabbixClientError(Exception):
    """ zabbix Error """


class ZabbixClient4_1():

    def __init__(self):
        self.url = settings.ZABBIX_SERVERURL
        self.username = settings.ZABBIX_USERNAME
        self.password = settings.ZABBIX_PASSWORD
        self.headers = settings.ZABBIX_HEADERS

    def get_token(self):
        payload = {"jsonrpc": "2.0",
                   "method": "user.login",
                   "params": {
                       "user": self.username,
                       "password": self.password
                   },
                   "id": 1,
                   "auth": None}
        try:
            response_result = self.do_request(payload)
            return response_result

        except KeyError as err:
            raise ZabbixClientError('user password error: %s' % str(err))

    def _build_request(self, method, params):
        payload = {"jsonrpc": "2.0",
                   "method": method,
                   "params": params,
                   "id": 1,
                   "auth": self.get_token()}
        return payload

    def do_request(self, pay_load):
        try:
            print("paylod sent to do request ", pay_load)
            r = requests.post(self.url, data=json.dumps(pay_load), headers=self.headers)
            r = r.json()
        except requests.exceptions.RequestException as err:
            raise ZabbixClientError('connection failed: %s' % str(err))
        print('response :', r['result'])
        return r['result']

    def parse_host_group_id(self, group_name):

        params = {
            "output": "extend",
            "filter": {
                "name": [
                    group_name
                ]
            }
        }
        request = self._build_request('hostgroup.get', params=params)
        raw_data = self.do_request(request)
        grpid = json.loads(json.dumps(raw_data[0]))
        return grpid['groupid']

    def check_existence_of_machine(self, name):

        params = {"filter": {
            "host": [
                name
            ]
        }
                 }
        request = self._build_request('host.get', params=params)
        response_result = self.do_request(request)
        print(response_result)
        if response_result == []:
            return True
        else:
            return False

    def by_host_ip(self, name):

        payload = {
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                "filter": {
                    "host": [
                        name
                    ]
                }
            },
            "id": 1,
            "auth": self.get_token()
        }

        response_result = self.do_request(payload)
        print(response_result)
        if response_result == []:
            return False
        else:
            return True



    def add_machine(self, name, ip):

        if check_chars(name) is True:
            if self.check_existence_of_machine(name) is True:
                if ip is not None:
                    params = {
                                 "host": name,
                                 "interfaces": [
                                     {
                                         "type": 2,
                                         "main": 1,
                                         "useip": 1,
                                         "ip": ip,
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
                                 "name": 'Delete_Me_' + name,
                                 "inventory_mode": 0,
                                 "inventory": {
                                     "macaddress_a": "01234",
                                     "macaddress_b": "56768"
                                 }
                             },
                    request = self._build_request('host.create', params=params)
                    self.do_request(request)
                    response = "added :" + name
                    return response
            else:
                response = "skipped :" + name
                return response



# p = ZabbixClient4_1()
# print("output of existence ", p.check_existence_of_machine('mesut'))
#
#
q = ZabbixClient4_1()
print("output of existence ", q.check_existence_of_machine('mobilenoc-fw/sec'))

q.add_machine('mobilenoc-fw/sec','4.71.144.117')