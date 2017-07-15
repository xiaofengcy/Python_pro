#!/usr/bin/python2
#-*- coding:utf-8 -*-
import urllib,hashlib
import random
import requests,sys
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfpage import PDFPage,PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams,LTTextBoxHorizontal
from pdfminer.converter import PDFPageAggregator
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def getTransText(text): #翻译
	q = text
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
	url = url.encode('UTF-8')
	res = requests.get(url)
	#转换为字典类型
	res = eval(res.text)
	return (res["trans_result"][0]['dst'])

def pdf_to_txt():
    fp = open("/home/xuna/桌面/python/1.pdf","rb")  #获取文档对象,把路径换成自己的就行，读写打开一个二进制文件
    parser = PDFParser(fp) #创建一个与文档相关联的解释器
    doc = PDFDocument(parser) #PDF文档对象存储文档结构
    if not doc.is_extractable: #检查文件是否允许文本提取
        raise PDFTextExtractionNotAllowed

    resource = PDFResourceManager(caching=False) #创建PDF资源管理器
    laparam = LAParams()    #参数分析器
    device = PDFPageAggregator(resource,laparams = laparam) #创建一个聚合器
    interpreter = PDFPageInterpreter(resource,device) #创建PDF页面解释器
    #循环遍历列表，每次处理一个page内容
    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)  #接受该页面的LTPage对象
        layout = device.get_result()
        #这里layout是一个LTPage对象，里面存放着这个page解析出的各种对象
        #一般包括LTTextBox,LTFigure,LTImage,LTTextBoxHorizontal等等
        result=""
        s=0
        for x in layout:
            #如果x是文本对象的话
            if(isinstance(x,LTTextBoxHorizontal)):
                with open('/home/xuna/桌面/python/3.txt','a') as f:
                    res1 = x.get_text()
                    result+=res1
                    result+='\n'
                    res1 = res1.replace('\n',' ') #处理换行

                    res2 = getTransText(res1).decode('unicode_escape').encode('utf8')
                    result+=res2
                    result+='\n'
                    f.write(result + '\n')
        return result
print pdf_to_txt()