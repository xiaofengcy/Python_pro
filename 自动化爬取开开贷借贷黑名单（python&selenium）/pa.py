# -*- coding:utf-8 -*-
#-*- coding:utf-8 -*-
import unittest
import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



url = "http://www.kaikaidai.com/Lend/Black.aspx"
driver = webdriver.Chrome()

#打开请求的url
driver.get(url)
f = open("/home/xuna/桌面/img_code/res.txt",'w')
a = 1
m = 1
x = 2
y = 12
while m <=38:
    elem = driver.find_element_by_name("rpMessage")
    elem.send_keys(m)
    elem.send_keys(Keys.RETURN)#模拟点击回车

    if m == 38:
        x=2
        y=10
    for n in range(x,y):
        print a
        name_xpath = '//*[@id="form1"]/div[3]/div/div[2]/div[4]/table[' + str(n) + ']/tbody/tr[1]/td[3]/a'
        name = driver.find_element_by_xpath(name_xpath).text

        id_xpath = '//*[@id="form1"]/div[3]/div/div[2]/div[4]/table[' + str(n) + ']/tbody/tr[2]/td[2]'
        id = driver.find_element_by_xpath(id_xpath).text

        adress_xpath = '//*[@id="form1"]/div[3]/div/div[2]/div[4]/table[' + str(n) + ']/tbody/tr[3]/td[2]'
        adress = driver.find_element_by_xpath(adress_xpath).text

        company_name_xpath = '//*[@id="form1"]/div[3]/div/div[2]/div[4]/table[' + str(n) + ']/tbody/tr[4]/td[2]'
        company_name = driver.find_element_by_xpath(company_name_xpath).text

        company_adress_xpath = '//*[@id="form1"]/div[3]/div/div[2]/div[4]/table[' + str(n) + ']/tbody/tr[5]/td[3]'
        company_adress = driver.find_element_by_xpath(company_adress_xpath).text

        email_xpath = '//*[@id="form1"]/div[3]/div/div[2]/div[4]/table[' + str(n) + ']/tbody/tr[1]/td[5]'
        email= driver.find_element_by_xpath(email_xpath).text

        call_xpath = '//*[@id="form1"]/div[3]/div/div[2]/div[4]/table[' + str(n) + ']/tbody/tr[2]/td[4]'
        call = driver.find_element_by_xpath(call_xpath).text

        phone_xpath = '//*[@id="form1"]/div[3]/div/div[2]/div[4]/table[' + str(n) + ']/tbody/tr[3]/td[4]'
        phone = driver.find_element_by_xpath(phone_xpath ).text
        try:
            save = name  + ";" + id + ";" + adress + ";" + company_name + ";" + company_adress + ";" + email + ";" + call + ";" + phone + "\n"
            f.write(save.encode("GB2312"))
            print save
            print type(save)
            a = a + 1
        except:
            print name,id,company_name,email,call,phone
            save = name  + ";" + id + ";" + "**" + ";" + company_name + ";" + "**" + ";" + email + ";" + call + ";" + phone + "\n"
            f.write(save.encode("GB18030"))
            print save
            print type(save)
            a = a + 1

    m = m + 1

driver.close()
