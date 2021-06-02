import requests

url = "https://www.baidu.com/s?wd=ip"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15(KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)'
}
page_text = requests.get(url=url,headers=headers,proxies={"https":'103.39.17.253:3128'}).text

with open('ip.html','w',encoding='utf-8') as fp:
    fp.write(page_text)
#反爬机制：封ip
#反反爬策略:使用代理进行请求发送