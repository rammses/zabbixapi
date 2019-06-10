from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class HostGroupSerializer(serializers.Serializer):
    groupname = serializers.CharField(required=True)


class HostGroupDetailsSerializer(serializers.Serializer):
    groupname = serializers.CharField(required=True)


class HostGroupIdSerializer(serializers.Serializer):
    groupname = serializers.CharField(required=True)


class DelHostGroupIdSerializer(serializers.Serializer):
    groupname = serializers.CharField(required=True)


class RenHostGroupNameSerializer(serializers.Serializer):
    old_name = serializers.CharField(required=True)
    new_name = serializers.CharField(required=True)


class HostTemplateSerializer(serializers.Serializer):
    hostid = serializers.CharField(required=True)


class GetHostNameSerializer(serializers.Serializer):
    host_name = serializers.CharField(required=True)


class GetHostsSerializer(serializers.Serializer):
    online_only = serializers.BooleanField(required=False)


class GetGroupsSerializer(serializers.Serializer):
    filters = serializers.CharField(required=False)


class HostAddSnmpSerializer(serializers.Serializer):
    host_name = serializers.CharField(required=True)
    snmp_interface_ip = serializers.IPAddressField(required=True)
    visible_name = serializers.CharField(required=True)

class AlarmsSerializer(serializers.Serializer):
    host_id = serializers.CharField(required=True)