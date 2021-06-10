import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from sunPro.items import SunproItem,DetailItem
#需求: 爬取sun网站中的编号和新闻标题、详情页中的新闻内容，编号
class SunSpider(CrawlSpider):
    name = 'sun'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://wz.sun0769.com/political/index/politicsNewest?id=1&page=1']
    #链接提取器:根据指定规则(allow = "正则")进行指定链接的提取
    link = LinkExtractor(allow=r'id=1&page=\d+')
    #https://wz.sun0769.com/political/politics/index?id=506066
    #https://wz.sun0769.com/political/politics/index?id=506063
    
    link_detail = LinkExtractor(restrict_xpaths='/html/body/div[2]/div[3]/ul[2]/li')

    rules = (
        #规则解析器:将链接提取器提取到的链接进行指定规则(callback)的解析操作
        Rule(link, callback='parse_item', follow=False),
        #follow = True：可以将链接提取器继续作用到链接提取器提取到的链接所对应的页面中
        Rule(link_detail,callback='parse_detail')
    )
    #解析新闻编号和新闻标题
    #如下两个解析方法中是不可以实现请求传参！
    #无法将两个解析方法解析的数据存储到同一个item中，可以依次存储到两个item
    def parse_item(self, response):
        #注意： xpath表达式中不可以出现tbody标签
        li_list = response.xpath('/html/body/div[2]/div[3]/ul[2]/li')
        for li in li_list:
            new_num = li.xpath('./span[1]/text()').extract_first()
            new_title = li.xpath('./span[3]/a/text()').extract_first()
            item = SunproItem()
            item['new_title'] = new_title
            item['new_num'] = new_num
            yield item
    #解析新闻内容和新闻编号
    def parse_detail(self,response):
        new_id = response.xpath('/html/body/div[3]/div[2]/div[2]/div[1]/span[4]/text()').extract_first()
        new_content = response.xpath('/html/body/div[3]/div[2]/div[2]/div[2]/pre/text()').extract_first()
        item = DetailItem()
        item['new_content'] = new_content
        item['new_id'] = new_id
        yield item