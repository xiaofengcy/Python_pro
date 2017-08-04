# -*-coding:utf-8 -*-
# Created: 07-06-2017 xuna
#   by Python 3.4.3  Sublime text 3(???)
#  _aurhor_ :xuna
import urllib.request ,sys
import re

provice = input('?????(?????):')
city = input('?????(?????):')
#?????url
url = "http://qq.ip138.com/weather/"+provice+'/'+city+'_7tian.htm'

#??????
weatherhtml = urllib.request.urlopen(url)
res = weatherhtml.read().decode('GB2312')

#???????
f=open('wea.txt','wb')
f.write(res.encode('GB2312'))
f.close()

#???????????
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
