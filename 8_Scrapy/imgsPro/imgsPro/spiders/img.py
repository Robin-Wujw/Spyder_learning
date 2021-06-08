import scrapy
from imgsPro.items import ImgsproItem

class ImgSpider(scrapy.Spider):
    name = 'img'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://sc.chinaz.com/tupian/']

    def parse(self, response):
        div_list = response.xpath('//*[@id="container"]/div')
        for div in div_list:
            #注意:解析的时候一定要使用伪属性
            img_src = div.xpath('./div/a/img/@src2').extract_first().split('_')[0]
            src = "https:"+ img_src + '.jpg'
            item = ImgsproItem()
            item['src'] = src 
            yield item