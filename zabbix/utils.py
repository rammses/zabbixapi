import json


class HostsIds:

    """
    in zabbix you use hostid for pretty much everything
    however you may need to use hostname, in this case
    you feed the hosts list to this class and find the
    required parameter
    """

    def get_hostid_from_names(self, list1, name):

        for member in list1:
            feed_json = json.dumps((member))
            jsonized_list = json.loads(feed_json)

            if jsonized_list['host'] == name:
                hostid = jsonized_list['hostid']
                return hostid

    def get_name_from_hostids(self, list1 ,hostid):

        for member in list1:
            feed_json = json.dumps((member))
            jsonized_list = json.loads(feed_json)

            if jsonized_list['hostid'] == hostid:
                name = jsonized_list['host']
                return name

