import scrapy
from bossPro.items import BossproItem


class BossSpider(scrapy.Spider):
    name = 'boss'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.zhipin.com/c100010000-p100101/']
    #https://www.zhipin.com/c100010000-p100101/?page=2&ka=page-2

    url = 'https://www.zhipin.com/c100010000-p100101/?page=%d'
    page_num = 2
    #回调函数接受item
    def parse_detail(self,response):
        item = response.meta['item']
        job_desc = response.xpath('//*[@id="main"]/div[2]/div/div[2]/div[2]/div[1]/div//text()').extract()
        job_desc = ''.join(job_desc)
        #print(job_desc)
        item['job_desc'] = job_desc
        yield item
    #解析首页中的岗位名称
    def parse(self, response):
        li_list = response.xpath('//*[@id="main"]/div/div[3]/ul/li')
        for li in li_list:
            item = BossproItem()
            job_name = li.xpath('./div/div[1]/div[1]/div/div[1]/span[1]/a/text()').extract_first()
            item['job_name'] = job_name
            detail_url = 'https://www.zhipin.com'+li.xpath('./div/div[1]/div[1]/div/div[1]/span[1]/a/@href').extract_first()
            print(job_name)
            #对详情页发请求获取详情页的页面源码数据
            #手动请求的发送
            #请求传参: meta={} 可以将meta字典传递给请求对应的回调函数
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})
        
        #分页操作
        if self.page_num <=3:
            new_url = format(self.url%self.page_num)
            self.page_num += 1

            yield scrapy.Request(new_url,callback=self.parse)