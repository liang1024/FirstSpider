from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from urllib.request import urlopen

# pip install pdfminer3k

# 获取文档对象(本地)
fp=open("big_letter_and_title.pdf","rb")
# 获取文档对象(网络)
fp=urlopen("https://www.tencent.com/zh-cn/articles/8003411490172512.pdf")

# 创建一个与文档关联的解释器
parser=PDFParser(fp)

# PDF文档的对象
doc=PDFDocument();

# 链接解释器和文档对象
parser.set_document(doc)
doc.set_parser(parser)

# 初始化文档
doc.initialize("")

# 创建PDF资源管理器
resoure=PDFResourceManager()

# 参数分析器
laparam=LAParams()

# 创建一个聚合器
device=PDFPageAggregator(resoure,laparams=laparam)

# 创建PDF页面解释器
interpreter=PDFPageInterpreter(resoure,device)

# 使用文档对象得到页面的集合
for page in doc.get_pages():
    #使用页面解释器来读取
    interpreter.process_page(page)

    #使用聚合器获取内容
    layout=device.get_result()

    for out in layout:
        if hasattr(out,"get_text"):
            print(out.get_text())

