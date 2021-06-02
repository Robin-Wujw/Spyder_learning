import requests
headers={
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15(KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)'
}
urls = [
"https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx",
'https://pic.qiushibaike.com/system/pictures/12436/124360753/medium/7TKGSDY0E3FBRC8Q.jpg'
]
def get_content(url):
    print('正在爬取',url)
    #get方法是一个阻塞的方法  
    response = requests.get(url=url,headers=headers)
    if response.status_code == 200:
        return response.content
def parse_content(content):
    print('响应数据的长度为:',len(content))
for url in urls:
    content = get_content(url)
    parse_content(content) 