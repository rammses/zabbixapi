from rest_framework import viewsets, response, status

from zabbix.serializers import \
    HostGroupSerializer, \
    HostGroupDetailsSerializer, \
    HostGroupIdSerializer, \
    DelHostGroupIdSerializer, \
    RenHostGroupNameSerializer,\
    GetHostNameSerializer,\
    GetHostsSerializer,\
    HostTemplateSerializer,\
    GetGroupsSerializer,\
    HostAddSnmpSerializer,\
    AlarmsSerializer

from MonitoringIntegration import settings
from zabbix.base import ZabbixClient4_1
import requests
import json
import sys


class Base:

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

    def list_groups(self, request):
        data = request.data
        serializer = GetGroupsSerializer(data=data)
        if serializer.is_valid():
            k = list(serializer.data.values())
            payload = {
                        "jsonrpc": "2.0",
                        "method": "hostgroup.get",
                        "params": {
                            "output": "extend",
                        },
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


class HostObjects(viewsets.ViewSet):

    def get_enabled_hosts(self, request):
        """
        lists enabled hosts
        :param request:
        :return: lists enabled machines and their zabbix hostids.
        """
        ZabbixClient = ZabbixClient4_1()
        response_result = ZabbixClient.get_enabled_hosts()

        return response.Response(data=response_result, status=status.HTTP_200_OK)


class HostObject(viewsets.ViewSet):

    def get_serializer(self, data=None):
        return GetHostNameSerializer(data=data)

    def get_host(self, request, host_name):
        print('detail :', host_name, ' end')
        print('request :', request.data, ' end')
        data = request.data
        serializer = self.get_serializer(data=data)
        print('after serializer :', serializer, ' end')
        # if serializer.is_valid():
        if host_name is not None:
            # k = list(serializer.data.values())
            payload = {
                        "jsonrpc": "2.0",
                        "method": "host.get",
                        "params": {
                                    "filter": {
                                            "host": [
                                                    host_name
                                                    ]
                                            }
                                },
                        "auth": Base.authenticate(),
                        "id": 1
                        }
            response_result = Base.Do_Request(payload)
            return response.Response(data=response_result, status=status.HTTP_200_OK)
        else:
            return response.Response(data=None, status=status.HTTP_204_NO_CONTENT)



class HostTemplates(viewsets.ViewSet):

    def get_serializer(self, data=None):
        return HostTemplateSerializer(data=data)

    def get_templates(self, request):
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            k = list(serializer.data.values())
            payload = {
                        "jsonrpc": "2.0",
                        "method": "host.get",
                        "params": {
                            "output": ["hostid"],
                            "selectParentTemplates": [
                                "templateid",
                                "name"
                            ],
                            "hostids": k[0]
                        },
                        "id": 1,
                        "auth": Base.authenticate()
                    }
            response_result = Base.Do_Request(payload)
            return response.Response(data=response_result, status=status.HTTP_200_OK)


class HostInterfaces(viewsets.ViewSet):


    def get_serializer(self, data=None):
        return HostTemplateSerializer(data=data)

    def get_interfaces(self, request):
        """
        Gets the detail of an inteface bound to host using it's name
        :param request:
        :return:
        """
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            values_from_request = list(serializer.data.values())

            zabbixclient = ZabbixClient4_1()
            response_result = zabbixclient.get_hosts_snmp_interface_by_name(values_from_request[0])

            return response.Response(data=response_result, status=status.HTTP_200_OK)


class HostStandardSnmp(viewsets.ViewSet):

    def get_serializer(self, data=None):
        return HostAddSnmpSerializer(data=data)

    def add_host(self, request):
        """
        Adds a host using hostname and snmp ip address
        :param request:
        :return:
        """
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            values_from_request = list(serializer.data.values())

            ZabbixClient = ZabbixClient4_1()
            response_result = ZabbixClient.add_machine(values_from_request[0], values_from_request[1])

            return response.Response(data=response_result, status=status.HTTP_200_OK)


class HostAlarms(viewsets.ViewSet):

    def get_serializer(self, data=None):
        return AlarmsSerializer(data=data)

    def list_host_alarms(self, request):
        """
        Lists alarms from zabbix usin host_id
        :param request:
        :return:
        """
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            values_from_request = list(serializer.data.values())
            print(values_from_request[0])

            ZabbixClient = ZabbixClient4_1()
            response_result = ZabbixClient.list_host_alarms(values_from_request[0])

            return response.Response(data=response_result, status=status.HTTP_200_OK)

    def acknowledge_alarm(self, request):
        pass

    def delete_alarm(self, request):
        pass


class CheckForHostsExistence(viewsets.ViewSet):
    """
    Checks that host exists on Zabbix
    if exists returns 200
    if not returns 204

    """

    def get_serializer(self, data=None):
        return GetHostNameSerializer(data=data)

    def by_host_name(self, request):

        data = request.data
        serializer = self.get_serializer(data=data)

        if serializer.is_valid():
            values_from_request = list(serializer.data.values())
            print(values_from_request[0])

            ZabbixClient = ZabbixClient4_1
            response_result = ZabbixClient.check_existence_of_machine(values_from_request[0])

            if response_result is not False:
                return response.Response(data='None', status=status.HTTP_204_NO_CONTENT)
            else:
                return response.Response(data=response_result, status=status.HTTP_200_OK)

