# 如何使用
# - 指定url
# - 发起请求
# - 获取响应数据
# - 持久化存储
import requests 
if __name__ == "__main__":
    #指定url
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15(KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)'
        }
    url = "https://www.sogou.com/"
    #发起请求
    #get方法会返回一个响应对象
    response = requests.get(url=url,headers=headers)
    #获取响应数据
    page_text = response.text
    print(page_text)
    #持久化存储
    with open('./sougou.html','w',encoding='utf-8') as fp:
        fp.write(page_text)
    print('爬取数据结束！')