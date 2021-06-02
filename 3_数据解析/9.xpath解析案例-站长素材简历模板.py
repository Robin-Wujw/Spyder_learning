# -*- coding:utf-8 -*-
import requests
from lxml import etree
import os 
if not os.path.exists('./rarLibs'):
    os.mkdir('./rarLibs')
if __name__ =="__main__":
    url = "https://sc.chinaz.com/jianli/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
    }
    for page in range(1,10):
        if page == 1:
            page_url = url+ 'free.html'
        else:
            page_url = url + 'free_' + str(page) + '.html'
        print(page_url)
        page_text = requests.get(url=page_url,headers=headers)
        page_text.encoding = page_text.apparent_encoding
        page_text = page_text.text
        tree = etree.HTML(page_text)
        # //*[@id="container"]/div[2]/p/a
        #//*[@id="container"]/div[3]/p/a
        ps_list = tree.xpath('//div[@id="main"]/div/div/p/a/@href')
        for li in ps_list:
            li = 'http:'+ li
            ps_text = requests.get(url=li,headers=headers)
            ps_text.encoding = ps_text.apparent_encoding
            ps_text = ps_text.text
            ps_tree = etree.HTML(ps_text)
            ps_rar_url =ps_tree.xpath('//*[@id="down"]/div[2]/ul/li[7]/a/@href')[0]
            ps_rar = requests.get(url=ps_rar_url,headers=headers).content
            ps_name = ps_tree.xpath('//div[@class="sc_warp clearfix"]/div/a[3]/text()')[0]
            ps_path= 'rarLibs/'+ ps_name+'.rar'
            with open(ps_path,'wb') as fp:
                fp.write(ps_rar)
                print(ps_name,'下载成功！')
