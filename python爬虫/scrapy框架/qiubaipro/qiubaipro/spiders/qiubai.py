import scrapy
from qiubaipro.items import QiubaiproItem

class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    # def parse(self, response):
    #     # 解析作者名称和段子内容
    #     data_all=[]
    #     for div in response.xpath('//div[@class="col1 old-style-col1"]/div'):
    #         # xpath返回的是selector的列表，使用extract()方法
    #         author=div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
    #         content=div.xpath('./a[1]/div/span//text()').extract()
    #         content=''.join(content)
    #         dic={
    #             'author':author,
    #             'content':content
    #         }
    #         data_all.append(dic)
    #     return data_all


    def parse(self, response):
        # 解析作者名称和段子内容
        data_all=[]
        for div in response.xpath('//div[@class="col1 old-style-col1"]/div'):
            # xpath返回的是selector的列表，使用extract()方法
            author=div.xpath('./div[1]/a[2]/h2/text() | ./div[1]/span/h2/text()')[0].extract()
            content=div.xpath('./a[1]/div/span//text()').extract()
            content=''.join(content)
            item = QiubaiproItem()
            item['author']=author
            item['content']=content

            yield item #item提交至管道