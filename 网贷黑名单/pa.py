# -*- coding:utf-8 -*-
#-*- coding:utf-8 -*-
import unittest
import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import sys
reload(sys)
sys.setdefaultencoding("ISO-8859-1")

def get_all_code():
    f = open("/home/xuna/桌面/img_code/all.txt",'w')
    url = 'http://www.p2pjd.com/News/20433.html'
    driver = webdriver.Chrome()
    driver.get(url)
    n =1
    for i in range(113):
        name_xpath = '//*[@id="content"]'
        name = driver.find_element_by_xpath(name_xpath).text.encode("GB18030","ignore")
        name = "".join(name.split())
        try:
            f.write(name + "\n")
        except:
            print "cuowu"
        print n
        n = n + 1

        if i == 112:
            break
        click_btn = driver.find_element_by_xpath('//*[@id="web2l"]/div[4]/li[1]/a')
        ActionChains(driver).click(click_btn).perform()

    driver.close()


def get_num():

    f = open("/home/xuna/桌面/img_code/all.txt",'r')
    f1 = open("/home/xuna/桌面/img_code/phone_number.txt",'a')
    s = ""
    for line in f:
        temp = line.decode("GB18030","ignore")
        s = s + temp

    #手机号
    t = set()
    res = re.findall(r'1[3458]\d{9}',s) + re.findall(r'\d{3}-\d{8}|\d{4}-\{7,8}',s) + re.findall(r'[1-9][0-9]{4,9}',s)

    #去重
    for num in res:
        t.add(num)

    for num in t:
        f1.write(str(num) + "\n")
    print len(t)


if __name__ == "__main__":

    #获取全部的数据
    #get_all_code()

    #依次获取数据中的手机号，电话号和QQ号
    get_num()
