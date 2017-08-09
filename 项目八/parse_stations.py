# !usr/bin/env/python3.5.2
# -*- coding:utf-8 -*-
import requests
import re  #正则表达式的包
from pprint import pprint

def main():
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9023'
    r = requests.get(url, verify = False)
    #verify = False 禁止证书验证
    #print (r.text)
    pattern = u'([\u4e00-\u9fa5]+)\|([A-Z]+)'
    #print (re.findall(pattern,r.text))
    result = dict(re.findall(pattern, r.text))
    #print (dict(result))
    print (result.keys())
    print (result.values())

if __name__ == "__main__":
    main()
