#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json


def get_connect():
    url = "https://lgn.bjut.edu.cn"
    data = {"DDDDD": "S201761811", "upass": "2356002", "v46s": "1", "v6ip": "", "f4serip": "172.30.201.10",
            "0MKKey": ""}
    response = requests.post(url, data=data)
    return response.text


def get_data():
    url = "http://123.127.175.45:8082/ajax/GwtWaterHandler.ashx"
    data = {"Method": "SelectRealData"}
    response = requests.post(url, data=data)
    return response.text


def data_parser(raw_data):
    data_list = []
    pop_data = json.loads(raw_data)
    for pop_dict in pop_data:
        siteNames = ['北京', '天津', '河北']
        if any(x in pop_dict['siteName'] for x in siteNames):
            data_list.append(pop_dict)
    return data_list


if __name__ == '__main__':
    res = get_connect()
    print("test")
    print(res)
    print(res.encode('utf-8'))
    # raw_data = get_data()
    # print(raw_data)

    # list = data_parser(raw_data)
    # for i in list:
    # print(i)
