# !usr/bin/env/python3.5.2
# -*- coding:utf-8 -*-
"""
火车票实时查看器

Usage:
    ticket [-dgktz] <from> <to> <date>

Options:
    -h --help     Show this screen.
    -d            动车
    -g            高铁
    -k            快速
    -t            特快
    -z            直达
"""
import requests
import json
from docopt import docopt
import stations
from prettytable import PrettyTable #Python通过PrettyTable模块可以将输出内容如表格方式整齐地输出
from colorama import Fore #命令行着色工具 Fore字体颜色
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def cli():
    arguments = docopt(__doc__, version = 'tickets 1.0')
    from_station = stations.get_telecode(arguments.get('<from>'))
    to_station = stations.get_telecode(arguments.get('<to>'))
    date = arguments.get('<date>')
    options = ''.join([key for key, value in arguments.items() if value is True])
    url = ( 'https://kyfw.12306.cn/otn/leftTicket/query?'
            'leftTicketDTO.train_date={}&'
            'leftTicketDTO.from_station={}&'
            'leftTicketDTO.to_station={}&'
            'purpose_codes=ADULT').format(date, from_station, to_station)
    r = requests.get(url, verify=False)
    raw_trains = r.json()['data']['result']
    pt = PrettyTable()
    pt._set_field_names('车次 车站 时间 历时 商务座 一等座 二等座 高级软卧 软卧 动卧 硬卧 软座 硬座 无座'.split())

    for raw_train in raw_trains:
        data_list = raw_train.split('|')
        train_no = (data_list[3]) #车次
        initial = train_no[0].lower()
        if initial in options or not options:
            from_station_code= (data_list[6])
            to_station_code= (data_list[7])
            from_station_name =''
            to_station_name= ''
            start_time = data_list[8]
            arrive_time = data_list[9]
            time_duration = data_list[10]
            normal_seat = data_list[32] or '--'
            first_class_seat = data_list[31] or '--'
            second_class_seat = data_list[30] or '--'
            ssoft_sleep = data_list[21] or '--'
            soft_sleep = data_list[23] or '--' #为空显示--
            move_sleep = data_list[33] or '--'
            hard_sleep = data_list[28] or '--'
            soft_seat = data_list[24 ] or '--'
            hard_seat = data_list[29] or '--'
            no_seat = data_list[26] or '--'
            #显示
            pt.add_row([
                ''.join([Fore.RED + train_no + Fore.RESET]),
                '\n'.join([Fore.GREEN + stations.get_name(from_station_code) + Fore.RESET,Fore.YELLOW + stations.get_name(to_station_code)+ Fore.RESET ]),
                '\n'.join([Fore.GREEN + start_time + Fore.RESET, Fore.YELLOW + arrive_time + Fore.RESET]),
                time_duration,
                normal_seat,
                first_class_seat,
                second_class_seat,
                ssoft_sleep,
                soft_sleep,
                move_sleep,
                hard_sleep,
                soft_seat,
                hard_seat,
                no_seat
              ])
    return pt

if __name__ == '__main__':
    res = cli()
    print (res)
