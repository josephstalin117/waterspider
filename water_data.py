#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
from pprint import pprint
import os

# def get_connect():
#     url = "https://lgn.bjut.edu.cn"
#     data = {"DDDDD": "S201761811", "upass": "2356002", "v46s": "1", "v6ip": "", "f4serip": "172.30.201.10",
#             "0MKKey": ""}
#     response = requests.post(url, data=data)
#     return response.text

def log_in():
    os.system("./home/user/login_bjut.sh")
def log_out():
    os.system("./home/user/logout_bjut.sh")
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
    data_str=''.join(str(e) for e in data_list)
    return data_str

def data_save(data,save_file):
    f=open(save_file,'a')
    f.write(data+ '\n')
    f.close()



if __name__ == '__main__':
    log_in()
#    res = get_connect()
    raw_data = get_data()
    # print(raw_data)
    log_out()
    data = data_parser(raw_data)
    print(data)
    # data.join('\n')
    data_save(data,"waterdata.txt")

    # for i in list:
    # print(i)
    # with open('ccc','w') as f:
#     for i in article1:
#         print(i, file=f)
#         wr = csv.writer(f, quoting=csv.QUOTE_ALL)
#         wr.writerow(mylist)
