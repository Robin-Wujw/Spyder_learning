#需求： 爬取糗事百科中糗图板块下所有的糗图图片
import requests
import re
import os 
if __name__ == '__main__':
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15(KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)'
    }
    if not os.path.exists('./qiutuLibs'):
        os.mkdir('./qiutuLibs')
    #设置一个通用的url模板
    url = 'https://www.qiushibaike.com/imgrank/page/%d/'
    for pageNum in range(1,14):
        #对应页码的url
        new_url = format(url%pageNum)
        page_text = requests.get(url=new_url,headers=headers).text
    #使用聚焦爬虫将页面中所有的糗图进行解析/提取
        ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
        image_src_list = re.findall(ex,page_text,re.S)
        #print(image_src_list)
        for src in image_src_list:
            #拼接出一个完整的图片url
            src = 'https:'+ src
            #请求到了图片的二进制数据
            img_data = requests.get(url=src,headers=headers).content
            #生成图片名称
            img_name = src.split('/')[-1]
            #图片存储路径
            imgPath = './qiutuLibs/'+img_name
            with open(imgPath,'wb') as fp:
                fp.write(img_data)
                print(img_name,'下载成功！')