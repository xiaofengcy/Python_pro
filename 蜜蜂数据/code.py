# -*- coding:utf-8 -*-
#-*- coding:utf-8 -*-
import unittest
import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def p2p():
    f1 = open("/home/xuna/桌面/img_code/p2p.txt",'w')

    for n in range(1,11):
        name_xpath = '/html/body/div[2]/div[2]/div/div[2]/div[1]/table/tbody/tr[' + str(n) + ']/td[1]'
        name = driver.find_element_by_xpath(name_xpath).text

        id_xpath = '/html/body/div[2]/div[2]/div/div[2]/div[1]/table/tbody/tr[' + str(n) + ']/td[2]'
        id = driver.find_element_by_xpath(id_xpath).text


        source_xpath = '/html/body/div[2]/div[2]/div/div[2]/div[1]/table/tbody/tr[' + str(n) + ']/td[3]'
        source= driver.find_element_by_xpath(source_xpath).text

        money_xpath = '/html/body/div[2]/div[2]/div/div[2]/div[1]/table/tbody/tr[' + str(n) + ']/td[4]'
        money= driver.find_element_by_xpath(money_xpath).text

        day_xpath = '/html/body/div[2]/div[2]/div/div[2]/div[1]/table/tbody/tr[' + str(n) + ']/td[5]'
        day = driver.find_element_by_xpath(day_xpath).text

        lend_xpath = '/html/body/div[2]/div[2]/div/div[2]/div[1]/table/tbody/tr[' + str(n) + ']/td[6]'
        lend = driver.find_element_by_xpath(lend_xpath).text


        save = name + ";" + id + ";" + source + ";" + money + ";" + day + ";" + lend + "\n"
        f1.write(save.encode("utf-8"))
        print save

def no_trust():
    f2 = open("/home/xuna/桌面/img_code/no_trust.txt",'w')
    for n in range(1,11):
        name_xpath = '/html/body/div[2]/div[2]/div/div[2]/div[2]/table/tbody/tr[' + str(n) + ']/td[1]'
        name = driver.find_element_by_xpath(name_xpath).text

        id_xpath = '/html/body/div[2]/div[2]/div/div[2]/div[2]/table/tbody/tr[' + str(n) + ']/td[2]'
        id = driver.find_element_by_xpath(id_xpath).text


        thing_xpath = '/html/body/div[2]/div[2]/div/div[2]/div[2]/table/tbody/tr[' + str(n) + ']/td[3]'
        thing = driver.find_element_by_xpath(thing_xpath).text

        trust_xpath = '/html/body/div[2]/div[2]/div/div[2]/div[2]/table/tbody/tr[' + str(n) + ']/td[4]'
        trust= driver.find_element_by_xpath(trust_xpath).text


        save = name + ";" + id + ";" + thing + ";" + trust + "\n"
        f2.write(save.encode("utf-8"))
        print save
    pass

if __name__=="__main__":

    url = "http://www.51zhengxin.com/front/queryBlackList.html"
    driver = webdriver.Chrome()
    driver.get(url)

    #P2P黑名单
    p2p()

    #模拟单击跳转到"失信被执行名单"
    click_btn = driver.find_element_by_xpath('//*[@id="tab-item-2"]')  # 单击按钮
    ActionChains(driver).click(click_btn).perform()  # 链式用法

    #失信被执行名单
    no_trust()

    driver.close()
