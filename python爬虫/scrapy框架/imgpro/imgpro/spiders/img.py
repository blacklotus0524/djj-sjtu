import scrapy
from imgpro.items import ImgproItem

class ImgSpider(scrapy.Spider):
    name = 'img'
    # allowed_domains = ['www.xxxx.com']
    start_urls = ['https://sc.chinaz.com/tupian/']

    def parse(self, response):
        div_list=response.xpath('//*[@id="container"]/div')
        for div in div_list:
            # 图片懒加载，使用伪属性
            src = div.xpath('./div/a/img/@src2').extract_first()
            item = ImgproItem()
            item['src'] = 'https:'+src
            yield item
