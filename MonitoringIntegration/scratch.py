import json

raw_data = [
  {
    "itemid": "37982",
    "clock": "1561393390",
    "value": "8",
    "ns": "639661000"
  },
  {
    "itemid": "37982",
    "clock": "1561393331",
    "value": "8",
    "ns": "37531800"
  },
  {
    "itemid": "37982",
    "clock": "1561393270",
    "value": "7",
    "ns": "622615700"
  },
  {
    "itemid": "37982",
    "clock": "1561393240",
    "value": "7",
    "ns": "219121900"
  },
  {
    "itemid": "37982",
    "clock": "1561393210",
    "value": "7",
    "ns": "267188000"
  },
  {
    "itemid": "37982",
    "clock": "1561393180",
    "value": "15",
    "ns": "388794200"
  },
  {
    "itemid": "37982",
    "clock": "1561393150",
    "value": "15",
    "ns": "946137800"
  },
  {
    "itemid": "37982",
    "clock": "1561393120",
    "value": "7",
    "ns": "548827400"
  },
  {
    "itemid": "37982",
    "clock": "1561393090",
    "value": "7",
    "ns": "405191200"
  },
  {
    "itemid": "37982",
    "clock": "1561393060",
    "value": "7",
    "ns": "319855400"
  },
  {
    "itemid": "37982",
    "clock": "1561393030",
    "value": "7",
    "ns": "236242800"
  },
  {
    "itemid": "37982",
    "clock": "1561393001",
    "value": "7",
    "ns": "33947900"
  },
  {
    "itemid": "37982",
    "clock": "1561392970",
    "value": "7",
    "ns": "222218100"
  },
  {
    "itemid": "37982",
    "clock": "1561392940",
    "value": "8",
    "ns": "381441600"
  },
  {
    "itemid": "37982",
    "clock": "1561392910",
    "value": "8",
    "ns": "387340300"
  },
  {
    "itemid": "37982",
    "clock": "1561392880",
    "value": "8",
    "ns": "240031300"
  },
  {
    "itemid": "37982",
    "clock": "1561392850",
    "value": "8",
    "ns": "303078800"
  },
  {
    "itemid": "37982",
    "clock": "1561392820",
    "value": "7",
    "ns": "736098500"
  },
  {
    "itemid": "37982",
    "clock": "1561392790",
    "value": "7",
    "ns": "277488600"
  },
  {
    "itemid": "37982",
    "clock": "1561392761",
    "value": "7",
    "ns": "25933500"
  },
  {
    "itemid": "37982",
    "clock": "1561392730",
    "value": "7",
    "ns": "467288200"
  },
  {
    "itemid": "37982",
    "clock": "1561392700",
    "value": "9",
    "ns": "583166300"
  },
  {
    "itemid": "37982",
    "clock": "1561392670",
    "value": "9",
    "ns": "968856900"
  },
  {
    "itemid": "37982",
    "clock": "1561392640",
    "value": "7",
    "ns": "347883600"
  },
  {
    "itemid": "37982",
    "clock": "1561392610",
    "value": "7",
    "ns": "241132500"
  },
  {
    "itemid": "37982",
    "clock": "1561392580",
    "value": "7",
    "ns": "425638200"
  },
  {
    "itemid": "37982",
    "clock": "1561392550",
    "value": "7",
    "ns": "912340900"
  },
  {
    "itemid": "37982",
    "clock": "1561392520",
    "value": "7",
    "ns": "260199700"
  },
  {
    "itemid": "37982",
    "clock": "1561392490",
    "value": "7",
    "ns": "562936800"
  },
  {
    "itemid": "37982",
    "clock": "1561392460",
    "value": "7",
    "ns": "690977500"
  },
  {
    "itemid": "37982",
    "clock": "1561392430",
    "value": "7",
    "ns": "984149800"
  },
  {
    "itemid": "37982",
    "clock": "1561392400",
    "value": "8",
    "ns": "387998800"
  },
  {
    "itemid": "37982",
    "clock": "1561392370",
    "value": "8",
    "ns": "220591400"
  },
  {
    "itemid": "37982",
    "clock": "1561392340",
    "value": "7",
    "ns": "315355700"
  },
  {
    "itemid": "37982",
    "clock": "1561392310",
    "value": "7",
    "ns": "307164400"
  },
  {
    "itemid": "37982",
    "clock": "1561392280",
    "value": "7",
    "ns": "371077700"
  },
  {
    "itemid": "37982",
    "clock": "1561392250",
    "value": "7",
    "ns": "609395400"
  },
  {
    "itemid": "37982",
    "clock": "1561392220",
    "value": "7",
    "ns": "747248200"
  },
  {
    "itemid": "37982",
    "clock": "1561392190",
    "value": "7",
    "ns": "292770800"
  },
  {
    "itemid": "37982",
    "clock": "1561392160",
    "value": "7",
    "ns": "722761500"
  },
  {
    "itemid": "37982",
    "clock": "1561392130",
    "value": "8",
    "ns": "456145800"
  },
  {
    "itemid": "37982",
    "clock": "1561392100",
    "value": "8",
    "ns": "753138000"
  },
  {
    "itemid": "37982",
    "clock": "1561392070",
    "value": "7",
    "ns": "269154400"
  },
  {
    "itemid": "37982",
    "clock": "1561392041",
    "value": "7",
    "ns": "31104400"
  },
  {
    "itemid": "37982",
    "clock": "1561392010",
    "value": "7",
    "ns": "322372000"
  },
  {
    "itemid": "37982",
    "clock": "1561391980",
    "value": "7",
    "ns": "997665500"
  },
  {
    "itemid": "37982",
    "clock": "1561391950",
    "value": "8",
    "ns": "404112900"
  },
  {
    "itemid": "37982",
    "clock": "1561391921",
    "value": "8",
    "ns": "44404500"
  },
  {
    "itemid": "37982",
    "clock": "1561391890",
    "value": "7",
    "ns": "372854200"
  },
  {
    "itemid": "37982",
    "clock": "1561391860",
    "value": "7",
    "ns": "676606600"
  },
  {
    "itemid": "37982",
    "clock": "1561391830",
    "value": "7",
    "ns": "892408100"
  },
  {
    "itemid": "37982",
    "clock": "1561391800",
    "value": "7",
    "ns": "317087500"
  },
  {
    "itemid": "37982",
    "clock": "1561391770",
    "value": "9",
    "ns": "287922700"
  },
  {
    "itemid": "37982",
    "clock": "1561391740",
    "value": "9",
    "ns": "354311700"
  }
]

"""
 {
    "itemid": "37982",
    "clock": "1561393390",
    "value": "8",
    "ns": "639661000"
  },
  """



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
              "2h": 120,
              "1d": 1440,
              "2d": 2880
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
        # print('insufficient data', error)
        average = average

    zone = average / retention_period
    print(zone)
    result.update({item: zone})
  return result

print(fetch_and_calculate_average_v2(raw_data))

