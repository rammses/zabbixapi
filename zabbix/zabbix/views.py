from rest_framework import viewsets, response, status
from zabbix.zabbix.serializers import LoginSerializer
from zabbix.zabbix.serializers import \
    HostGroupSerializer, \
    HostGroupDetailsSerializer, \
    HostGroupIdSerializer, \
    DelHostGroupIdSerializer, \
    RenHostGroupNameSerializer,\
    GetHostNameSerializer,\
    GetHostsSerializer
# HostSerializer
from MonitoringIntegration import settings
import requests
import json
import sys


class Base:

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

class HostGroupObject(viewsets.ViewSet):

    def get_serializer(self, data=None):
        return HostGroupSerializer(data=data)

    def add_group(self, request):
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            k = list(serializer.data.values())

            payload = {
                "jsonrpc": "2.0",
                "method": "hostgroup.create",
                "params": {
                    "name": k[0]
                },
                "auth": Base.authenticate(),
                "id": 1
            }
            response_result = Base.Do_Request(payload)
            return response.Response(data=response_result, status=status.HTTP_200_OK)

    def get_group(self, request):
        data = request.data
        serializer = HostGroupIdSerializer(data=data)
        if serializer.is_valid():
            k = list(serializer.data.values())
            payload = {
                "jsonrpc": "2.0",
                "method": "hostgroup.get",
                "params": {
                    "output": "extend",
                    "filter": {
                        "name": [
                            k[0]
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
            return response.Response(data=grpid['groupid'], status=status.HTTP_200_OK)

    def delete_group(self, request):
        data = request.data
        serializer = DelHostGroupIdSerializer(data=data)
        if serializer.is_valid():
            k = list(serializer.data.values())
            delgroupid = Base.ParseHostGroupId(k[0])
            payload = {
                "jsonrpc": "2.0",
                "method": "hostgroup.delete",
                "params": [
                    delgroupid,
                ],
                "auth": Base.authenticate(),
                "id": 1
            }
            response_result = Base.Do_Request(payload)
            return response.Response(data=response_result, status=status.HTTP_200_OK)

class HostGroupRename(viewsets.ViewSet):
    def get_serializer(self, data=None):
        return RenHostGroupNameSerializer(data=data)

    def rename_group(self, request):
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            k = list(serializer.data.values())
            old_name = k[0]
            new_name = k[1]
            print(old_name, new_name)
            rengroupname = Base.ParseHostGroupId(old_name)
            payload = {
                "jsonrpc": "2.0",
                "method": "hostgroup.update",
                "params": {
                    "groupid": rengroupname,
                    "name": new_name
                },
                "auth": Base.authenticate(),
                "id": 1
            }
            response_result = Base.Do_Request(payload)
            return response.Response(data=response_result, status=status.HTTP_200_OK)

class HostObject(viewsets.ViewSet):

    def get_serializer(self, data=None):
        return GetHostNameSerializer(data=data)

    def get_host(self, request):
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            k = list(serializer.data.values())
            payload = {
                        "jsonrpc": "2.0",
                        "method": "host.get",
                        "params": {
                                    "filter": {
                                            "host": [
                                                    k[0]
                                                    ]
                                            }
                                },
                        "auth": Base.authenticate(),
                        "id": 1
                        }
            response_result = Base.Do_Request(payload)
            # R = requests.post(settings.ZABBIX_SERVERURL, data=json.dumps(payload), headers=settings.ZABBIX_HEADERS)
            # R = R.json()
            # raw_data = R['result']
            # print(raw_data)
            # host_details = json.loads(json.dumps(raw_data[0]))
            # print(host_details)
            return response.Response(data=response_result, status=status.HTTP_200_OK)

class HostObjects(viewsets.ViewSet):
    def get_serializer(self, data=None):
        return GetHostsSerializer(data=data)

    def get_hosts(self, request):
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            k = list(serializer.data.values())
            if k[0] == True:
                print("online devices only")
                payload = {
                    "jsonrpc": "2.0",
                    "method": "host.get",
                    "params": {
                        "output": ["host"],
                        "status": ["1"],
                    },
                    "id": 2,
                    "auth": Base.authenticate()
                }
            else:
                print("all devices")
                payload ={
                            "jsonrpc": "2.0",
                            "method": "host.get",
                            "params": {
                                    "output": ["host"],
                                    },
                            "id": 2,
                            "auth": Base.authenticate()
                }

            response_result = Base.Do_Request(payload)
            return response.Response(data=response_result, status=status.HTTP_200_OK)

class HostAlarms(viewsets.ViewSet):

    def get_serializer(self, data=None):
        return GetHostsSerializer(data=data)

    def get_alarms(self, request):
        pass

    def acknowledge_alarm(self, request):
        pass

    def delete_alarm(self, request):
        pass

class SnmpHostAddStandard:

    def get_serializer(self, data=None):
        return GetHostsSerializer(data=data)


