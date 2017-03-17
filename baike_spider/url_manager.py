class UrlManager(object):
    def __init__(self):
        self.new_urls = set()  # 未爬取过的URl队列
        self.old_urls = set()  # 爬取过的Url队列

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, new_urls):
        if new_urls is None or len(new_urls) == 0:
            return
        for url in new_urls:
            self.add_new_url(url)

    #获取一个新的URL   pop():从队列中取出的同时,从原队列中移除
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    # 判断是否有新的URL
    def has_new_url(self):
        return len(self.new_urls) != 0
