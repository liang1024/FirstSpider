from bs4 import BeautifulSoup
import re
import urllib.parse


class HtmlParser(object):
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, "html.parser",from_encoding='UTF-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    # 获取页面中的新URl
    def _get_new_urls(self, page_url, soup):
        new_urls = set()

        # links = soup.find_all('a', href=re.compile(r'/view/\d+\.htm'))
        links = soup.find_all('a', href=re.compile(r"/item/"))
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    # 获取数据
    def _get_new_data(self, page_url, soup):
        res_data = {}

        # url
        res_data['url'] = page_url
        # print('页面的ur：',page_url)

        # <dd class="lemmaWgt-lemmaTitle-title">
        # <h1>自由软件</h1>

        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        # print('标题节点：',title_node.get_text())
        res_data['title'] = title_node.get_text()

        # <div class="lemma-summary" label-module="lemmaSummary">

        summary_node = soup.find('div', class_='lemma-summary')
        # print('摘要节点：',summary_node.get_text())
        res_data['summary'] = summary_node.get_text()

        return res_data
