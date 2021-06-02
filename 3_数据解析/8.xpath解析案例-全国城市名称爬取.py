# -*- coding:utf-8 -*-
import requests
from lxml import etree
import os 
if __name__ =="__main__":
    # url = "https://www.aqistudy.cn/historydata/"
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
    # }
    # page_text = requests.get(url=url,headers=headers).text


    # #数据解析:src的属性值 alt属性
    # tree = etree.HTML(page_text)
    # hot_li_list = tree.xpath('//div[@class="bottom"]/ul/li')
    # #创建一个文件夹
    # if not os.path.exists('./picLibs'):
    #     os.mkdir('./picLibs')
    # all_city_names = []
    # #解析到了热门城市的城市名称
    # for li in hot_li_list:
    #     hot_city_name = li.xpath('./a/text()')[0]
    #     all_city_names.append(hot_city_name)
    # city_names_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
    # #解析的是全部城市的名称
    # for li in city_names_list:
    #     city_name = li.xpath('./a/text()')[0]
    #     all_city_names.append(city_name)
    # print(all_city_names,len(all_city_names))
    url = "https://www.aqistudy.cn/historydata/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
    }
    page_text = requests.get(url=url,headers=headers).text


    #数据解析:src的属性值 alt属性
    tree = etree.HTML(page_text)
    #解析到热门城市和所有城市对应的a标签
    # div/ul/li/a 
    # div/ul/div[2]/li/a
    a_list = tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
    all_city_names = []
    for a in a_list:
        city_name = a.xpath('./text()')[0]
        all_city_names.append(city_name)
    print(all_city_names,len(all_city_names))