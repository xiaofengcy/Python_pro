# -*- coding:utf-8
import urllib2

class HtmlDownLoader(object):

    def download(self, url):
        if url is None:
            return None

        #直接请求
        response = urllib2.urlopen(url)

        #获取状态码，200表示获取成功，404失败
        if response.getcode() !=200:
            return None
        else:
            return response.read() #返回获取内容
