import scrapy


class QuotesSpider(scrapy.Spider):
    # 识别蜘蛛。它在项目中必须是唯一的，也就是说，您不能为不同的Spiders设置相同的名称。
    name = "quotes"

    # 必须返回一个可迭代的请求（您可以返回一个请求列表或写一个生成器函数），Spider将开始爬行。随后的请求将从这些初始请求连续生成。
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    # 一种将被调用来处理为每个请求下载的响应的方法。response参数是一个TextResponse保存页面内容的实例，并且还有其他有用的方法来处理它。
    # 该parse()方法通常解析响应，将刮取的数据提取为示例，并且还可以查找新的URL以从中创建新的请求（Request）。
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)