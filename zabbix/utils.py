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


def fetch_and_calculate_average(data,retention):
  """
  gets list with json members uses value from every member returns average
  :param data: the list of values
  :param retention: 1m, 5m , 1h , 1d ,2d
  :return:
  """
  average = 0
  short_cut = {
              "1m": 1,
              "5m": 5,
              "1h": 60,
              "2h": 120,
              "1d": 1440,
              "2d": 2880
  }
  if retention in short_cut:
    retention = int(short_cut[retention])
  elif retention is None:
    retention = 1

  for count in range(int(retention)):

    try:
      load_json = json.dumps(data[count])
      jsonized = json.loads(load_json)
      # print(jsonized['value'])
      average=average+int(jsonized['value'])
    except IndexError as error:
      print('insufficient data', error)
      return 0

  result = average / retention
  return result


def fetch_and_calculate_average_v2(data):
  """
  gets list with json members uses value from every member returns average
  :param data: the list of values
  :param retention: 1m, 5m , 1h , 1d ,2d
  :return:
  """
  result = {}
  average = 0
  short_cut = {
              "1m": 1,
              "5m": 5,
              "1h": 60,
              "1d": 1440,
              "1w": 10080
  }
  for item in short_cut:
    retention_period= int(short_cut[item])
    print('step :', item)
    for count in range(retention_period):
      try:
        load_json = json.dumps(data[count])
        jsonized = json.loads(load_json)
        average = average + int(jsonized['value'])
      except IndexError as error:
        average = average

    zone = average / retention_period
    print(zone)
    result.update({item: zone})
  return result