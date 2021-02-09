import scrapy


class TestV1Spider(scrapy.Spider):
    # file name:爬虫文件的唯一标识
    name = 'test_v1'
    # 允许的域名:用来限定starturl中哪些可以进行请求发送
    # allowed_domains = ['wwww.xxxx.com']
    # 起始的url：该列表中存放的url会被scrapy自动进行请求的发送
    start_urls = ['https://wwww.baidu.com/','https://www.sogou.com']

    # 用于数据解析，respinse参数表示请求成功后对应的响应对象
    def parse(self, response):
        print(response)
