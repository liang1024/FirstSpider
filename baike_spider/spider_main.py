
# -*- coding: utf-8 -*-
from baike_spider import url_manager,html_pareser,html_downloader,html_outputer
'''
time: 2017-03-18
'''
class SpiderMain(object):

    def __init__(self):
        self.urls=url_manager.UrlManager()
        self.downloader=html_downloader.HtmlDownLoader()
        self.parser=html_pareser.HtmlParser()
        self.outputer=html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count=1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url=self.urls.get_new_url()
                print('craw %d:%s'%(count,new_url))
                html_cont=self.downloader.download(new_url)
                new_urls,new_data=self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count==1000:
                    break

                count=count+1
            except:
                print('craw failed ：')
            #     想看错误日志时，可使用这个
            # except Exception as e:
            #     print('craw failed ：',e)

        self.outputer.output_html()


if __name__=="__main__":
    root_url="http://baike.baidu.com/item/Python?sefr=cr"
    obj_spider=SpiderMain()
    obj_spider.craw(root_url)
