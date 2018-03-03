#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import os


def log_in():
    os.system("bash /home/user/login_bjut.sh>/dev/null")


def log_out():
    os.system("bash /home/user/logout_bjut.sh>/dev/null")


def get_data():
    url = "http://123.127.175.45:8082/ajax/GwtWaterHandler.ashx"
    data = {"Method": "SelectRealData"}
    response = requests.post(url, data=data)
    return response.text


def data_parser(raw_data):
    data_list = []
    pop_data = json.loads(raw_data)
    data_str = ''.join(str(e) for e in pop_data)
    return data_str


def data_save(data, save_file):
    f = open(save_file,'a',encoding='utf-8')
    result=data+'\n'
    f.write(result)
    f.close()


if __name__ == '__main__':
    log_in()
    raw_data = get_data()
    log_out()
    data = data_parser(raw_data)
    print(data)
    #data_save(data, "waterdata.txt")

