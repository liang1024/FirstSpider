from urllib import request
class HtmlDownLoader(object):
    def download(self, new_url):
        if new_url is None:
            return None
        response = request.urlopen(new_url)
        if response.getcode()!= 200:
            return None
        # print('下载的页面：',response.read())
        return response.read()
