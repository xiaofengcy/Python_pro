#/usr/bin/env python
#-*- coding:utf-8 -*-
 
import urllib,hashlib
import random
import requests,sys


def getTransText(in_text):
	q = in_text
	fromLang = 'auto'  #翻译源语言=自动检测
	toLang1 = 'auto'    #译文语言 = 自动检测

	appid = '20170711000064108'
	salt = random.randint(32768, 65536)
	secretKey = '0y2JkztWWwGFfgivKz2N' #密钥

    #生成sign
	sign = appid+q+str(salt)+secretKey
	#计算签名sign(对字符串1做md5加密，注意计算md5之前，串1必须为UTF-8编码)
	m1 = hashlib.md5(sign.encode('utf-8'))
	sign = m1.hexdigest()
     
    #计算完整请求
	myurl = '/api/trans/vip/translate'
	myurl = myurl+'?appid='+appid+'&q='+q+'&from='+fromLang+'&to='+toLang1+'&salt='+str(salt)+'&sign='+sign
	url = "http://api.fanyi.baidu.com"+myurl

    # 发送请求
	url = url.encode('utf-8')
	res = requests.get(url)

	#转换为字典类型
	res = eval(res.text)
	return (res["trans_result"][0]['dst'])
while(True):
	in_text=input()
	print (in_text+'  =  '+getTransText(in_text))