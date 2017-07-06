# -*-coding:utf-8 -*-
# Created: 07-06-2017 xuna
#   by Python 3.4.3  Sublime text 3(可交互)
#  _aurhor_ :xuna
import urllib.request ,sys
import re

provice = input('输入省份名（请使用拼音）：')
city = input('输入城市名（请使用拼音）：')
#获取天气的url
url = "http://qq.ip138.com/weather/"+provice+'/'+city+'_7tian.htm'

#获取页面信息
weatherhtml = urllib.request.urlopen(url)
res = weatherhtml.read().decode('GB2312')

#将获取信息写入
f=open('wea.txt','wb')
f.write(res.encode('GB2312'))
f.close()

#正则表达式获取天气信息
pattern = 'Title.+<b>(.+)</b>'
Title = re.search(pattern,res).group(1)

pattern = '>(\d*-\d*-\d*.+?)<'
date = re.findall(pattern,res)

pattern = 'alt="(.+?)"'
weather = re.findall(pattern,res)

print ("%35.30s"%Title)
length = len(date)
for i in range (0,length):
	print ('%33.20s'%date[i], '\t%s'%weather[i])
