from rest_framework import viewsets, response, status
from django.core import exceptions
from zabbix.utils import HostsIds,fetch_and_calculate_average_v2
from zabbix.models import Machines

from zabbix.serializers import \
    HostGroupSerializer, \
    HostGroupIdSerializer, \
    DelHostGroupIdSerializer, \
    RenHostGroupNameSerializer,\
    GetHostNameSerializer,\
    HostTemplateSerializer,\
    GetGroupsSerializer,\
    HostAddSnmpSerializer,\
    AlarmsSerializer

from MonitoringIntegration import settings
from zabbix.base import ZabbixClient4_1
from zabbix.utils import HostsIds
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


    def get_host(self, request, machine_id):

        if machine_id is not None:

            print(machine_id)
            id_ = machine_id
            try:
                ZabbixClient = ZabbixClient4_1()
                m = Machines.objects.get(id=int(id_))

                response_result = ZabbixClient.get_host_details(m.name)

                return response.Response(data=response_result, status=status.HTTP_200_OK)

            except exceptions.ObjectDoesNotExist:
                return response.Response(data="DB error", status=status.HTTP_204_NO_CONTENT)


    

        else:
            return response.Response(data=None, status=status.HTTP_204_NO_CONTENT)


class HostTemplates(viewsets.ViewSet):

    def get_serializer(self, data=None):
        return HostTemplateSerializer(data=data)

    def get_templates(self, request, machine_id):
        data = request.data
        if machine_id is not None:

            print(machine_id)
            id_ = machine_id
            try:
                ZabbixClient = ZabbixClient4_1()
                m = Machines.objects.get(id=int(id_))
                machine_list = ZabbixClient.get_enabled_hosts()
                host_id = HostsIds().get_hostid_from_names(machine_list, m.name)

                response_result = ZabbixClient.get_resource_template_of_host(host_id)

                return response.Response(data=response_result, status=status.HTTP_200_OK)

            except exceptions.ObjectDoesNotExist:
                return response.Response(data="DB error", status=status.HTTP_204_NO_CONTENT)

        else:
            return response.Response(data=None, status=status.HTTP_204_NO_CONTENT)

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
      
    def list_host_alarms(self, request, machine_id):

        """
        Lists alarms from zabbix using id
        :param request:
        :return:
        """


        if machine_id is not None:

            print(machine_id)
            id_ = machine_id
            try:
                ZabbixClient = ZabbixClient4_1()
                m = Machines.objects.get(id=int(id_))
                machine_list = ZabbixClient.get_enabled_hosts()
                host_id = HostsIds().get_hostid_from_names(machine_list, m.name)

                response_result = ZabbixClient.list_host_alarms(host_id)

                return response.Response(data=response_result, status=status.HTTP_200_OK)

            except exceptions.ObjectDoesNotExist:
                return response.Response(data="DB error", status=status.HTTP_204_NO_CONTENT)

        else:
            return response.Response(data=None, status=status.HTTP_204_NO_CONTENT)

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


class GetResourceDetails(viewsets.ViewSet):
    """
    zabbix
    """

    def processors(self, machine_id):

        if machine_id is not None:
            print(machine_id)
            id_ = machine_id
            try:
                ZabbixClient = ZabbixClient4_1()
                m = Machines.objects.get(id=int(id_))
                machine_list = ZabbixClient.get_enabled_hosts()
                host_id = HostsIds().get_hostid_from_names(machine_list, m.name)

                response_result = ZabbixClient.get_cpu_history(host_id)

                return response.Response(data=response_result, status=status.HTTP_200_OK)

            except exceptions.ObjectDoesNotExist:
                return response.Response(data="DB error", status=status.HTTP_204_NO_CONTENT)

        else:
            return response.Response(data=None, status=status.HTTP_204_NO_CONTENT)

        #calculate_average 5min 1 h 1 day 2 days
        #return json

        return

    def memory(self, machine_id):
        # get data taken 2 times per min with 5 sec average
        # calculate_average 5min 1 h 1 day 2 days
        # return json
        return

    def storage(self, machine_id):
        # get data
        # calculate_average 5min 1 h 1 day 2 days
        # return json
        return

class Items(viewsets.ViewSet):

    def get_items(self,request,keyname):

        """
        Lists items in zabbix
        """

        if keyname is not None:
            try:
                ZabbixClient = ZabbixClient4_1()
                response_result = ZabbixClient.get_items(keyname)
                return response.Response(data=response_result, status=status.HTTP_200_OK)

            except exceptions.ObjectDoesNotExist:
                return response.Response(data="DB error", status=status.HTTP_204_NO_CONTENT)

        else:
            print("")
            return response.Response(data="no keyname specified", status=status.HTTP_204_NO_CONTENT)


class HistoricData(viewsets.ViewSet):

    @staticmethod
    def get_item_id(host_id, key_name):
        if host_id or key_name is not None:
            ZabbixClient = ZabbixClient4_1()
            response_result = ZabbixClient.get_host_items(key_name,host_id)
            raw_data = response_result
            if len(raw_data) is not 0:
                data = json.loads(json.dumps(raw_data[0]))
                return data['itemid']
            else:
                return "0"
        else:
            return "0"

    def cpu_data(self,request, machine_id):
        """
        lists cpu historic data 5min, 1hour, 1 day, 2 day
        :param machine_id: machine id from database
        :return: json output 5min : "48", 1h : "70, 1day: "30", 2day: "14"
        """
        if machine_id is not None:
            id_ = machine_id
            try:
                ZabbixClient = ZabbixClient4_1()
                m = Machines.objects.get(id=int(id_))
                machine_list = ZabbixClient.get_enabled_hosts()
                host_id = HostsIds().get_hostid_from_names(machine_list, m.name)
                cpu_item = self.get_item_id(host_id, "cpu_load")
                response_result = ZabbixClient.get_cpu_history(host_id, cpu_item)

                calculations = fetch_and_calculate_average_v2(response_result)
                return response.Response(data=calculations, status=status.HTTP_200_OK)

            except exceptions.ObjectDoesNotExist:
                return response.Response(data="DB error", status=status.HTTP_204_NO_CONTENT)

        else:
            return response.Response(data=None, status=status.HTTP_204_NO_CONTENT)

    def used_ram_data(self,machine_id):
        return

    def free_ram_data(self,machine_id):
        return

    def ram_data(self,machine_id):
        return