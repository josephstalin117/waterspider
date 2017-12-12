import requests
import json

def getData():
    url="http://123.127.175.45:8082/ajax/GwtWaterHandler.ashx"
    data = {"Method":"SelectRealData"}
    response = requests.post(url, data=data)
    return response.text

def dataParser(raw_data):
    data_list=[]
    pop_data=json.loads(raw_data)
    for pop_dict in pop_data:
        siteNames=['北京','天津','河北']
        if any(x in pop_dict['siteName'] for x in siteNames):
            data_list.append(pop_dict)
    return data_list


if __name__ == '__main__':
    raw_data=getData()
    list=dataParser(raw_data)
    for i in list:
        print(i)
