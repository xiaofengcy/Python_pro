# coding:utf8
import url_manager, html_parser, html_downloader,html_outputer
class SpiderMain(object):

    def __init__(self):
        self.urls = url_manager.UrlManager() #url管理器
        self.downloader = html_downloader.HtmlDownLoader() #下载器
        self.parser = html_parser.HtmlParser() #解析器
        self.outputer = html_outputer.HtmlOutputer() #输出器

    def craw(self,root_url):
        count = 1

        #将入口url添加进url管理器（单个）
        self.urls.add_new_url(root_url)
        #启动爬虫的循环
        while self.urls.has_new_url():
            try:
                #获取待爬取的url
                new_url = self.urls.get_new_url()
                print 'craw %d : %s'%(count,new_url)
                #启动下载器下载html页面
                html_cont = self.downloader.download(new_url)


                #解析器解析得到新的url列表以及新的数据
                new_urls, new_data = self.parser.parse(new_url, html_cont)

                #将获取的新的url添加进管理器（批量)
                self.urls.add_new_urls(new_urls)
                #收集数据
                self.outputer.collect_data(new_data)
            except:
                print "craw failed!!!"


            if count == 1000:
                break
            count = count + 1
        #输出收集好的数据
        self.outputer.output_html()


if __name__=="__main__":
    #爬虫入口url
    root_url = "https://baike.baidu.com/item/Python"
    obj_spider = SpiderMain()
    #启动爬虫
    obj_spider.craw(root_url)
