import requests
from lxml import etree
if __name__=="__main__":
    etree = html.etree
    #爬取到页面源码数据
    url = 'https://bj.58.com/ershoufang/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
    }
    page_text = requests.get(url=url,headers=headers).text

    #数据解析
    tree = etree.HTML(page_text)
    #储存的是div对象
    li_list = tree.xpath('//section[@class="list"]/div')
    fp = open('58.txt','w',encoding='utf-8')
    for div in li_list:
        title = div.xpath('./a/div[2]/div//h3/text()')[0]
        fp.write(title+'\n')
    print("over...")
