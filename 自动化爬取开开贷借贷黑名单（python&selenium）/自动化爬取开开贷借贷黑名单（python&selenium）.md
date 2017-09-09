详细链接：http://blog.csdn.net/xunalove/article/details/77906343
需求
       
   网址：http://www.kaikaidai.com/Lend/Black.aspx
    1.获取每页的10个人的信息（每个人的信息包含8项），总378个名单，每页10个，共28页。、
    2.将数据保存在txt，一行包含一个人的八条信息，中间以分号”;”分隔，保存格式为如下：

            冯介伦；370724197209050338；山东省潍坊市临朐县冶源镇车家沟村107号；临朐县腾达天然大理石加工厂；临朐县冶源镇红光村南(无门牌        号）；lqfengjielun@163.com；05363332678；15065681089

 

实现方法

使用爬虫利器selenium获取页面每个元素的xpath内容（XPath是路径表达式，可以定位HTML中的元素，并获取元素的内容），最后模拟在页号框输入页码，模拟点击回车跳转令一页面。
获取元素xpath的方法（谷歌浏览器）：

            页面选中元素—-右击—-检查—-右击—copy

还有一点需要注意：在获取一页10人信息时，每个人xpath的路径会有联系，需要自己总结。

代码实现

    # -*- coding:utf-8 -*-
    """
    @author:xunalove
    date   : 2017-9-8
    python :2.7
    os :ubuntu 16.04
    Browse : Chrome
    """
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


数据爬取结果

                     赵辉;372501197608020319;聊城市三里铺风景小区3号楼3单元506;济南西车辆段聊城运用车间;聊城火车北站;95371392@qq.com;06358411571;15006389766
                     殷雪丽;370284198311206427;山东省青岛市黄岛区灵山卫观海华庭23号楼103;淄博水泥经销处;青岛市黄岛区海尔大道中国储运;754051573@qq.com;13276420673;13792896184
                     王金芳;37242219690627241x;山东省平原县王杲铺镇肖屯村305号;全旺家具厂;平原县王杲铺镇肖屯村;wangjinfang@163.com;15165343843;15165343843
                     高文国;37232319790327241X;山东省滨州市惠民县东景豪庭A区2号楼2单元801室;山东省惠民县爱书人文化传播有限公司;山东省滨州市惠民县东门大街南侧;13793865898@163.com;05435352799;13793865898
                     李明东;370919197112010014;山东省莱芜市莱城区凤城东大街115号赢中赢小区4号楼东单元1002;莱芜市贵福源建安工程有限公司;莱芜高新区凤城东大街115号;zaolanaa@163.com;13906340650;0
                     宋俊华;372526198209150433;山东青岛市黄岛区北江支路46号内1户;青岛思必得餐饮管理服务有限公司;青岛经济技术开发区沅江路6-1号;13510815@qq.com;053286880350;15865322195
                     郑晓华;37028319801108832x;山东省胶南市经济开发区大哨头村委会7号台区;黄岛区乐方快餐店;青岛市黄岛区（原胶南市）琅琊台南路122-4号;249707589@qq.com;13698668568;13698668568
                     李志强;372421197205063410;德州市开发区东风东路德百玫瑰园1号楼3单元1602;德州德瑞园林公司;德州市经济开发区德百物流怡家公寓AA层15室;lizhiqiang410@163.com;05342766996;13805341537
                     张丙华;372431197408306710;**;宁津县宁安特消声器厂;**;463308787@qq.com;05345421566;3953461358
                     刘道永;371202197508252912;山东省莱芜市莱城区汶河名邸28号东四单元102;莱芜市莱城区新瑞轮胎经营部;钢城区颜庄镇东红埠岭村;45451415@qq.com;0;18663400588


遇到的问题以及解决方法

1.页面的编码是“charset=GB2312”，保存txt中我们使用encode(“GB2312”),但是信息里面有一个人名为“ 王中堃”中的“堃”不在”GB2312”库中，导致编码错误？
解决方法：

    将编码"GB2312"改为"GB18030"。

2.地址中会出现“宁津县泉润·福宁壹号”中间点或者出现的“-”会编码错误？

    当出现这两类错误时，将地址置为“**”。

