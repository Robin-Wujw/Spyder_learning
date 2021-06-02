# 如何使用
# - 指定url
# - 发起请求
# - 获取响应数据
# - 持久化存储
#破解百度翻译
  # post请求 携带了 参数
  # 响应数据是一组json数据
#UA检测：门户网站的服务器会检测对应请求的载体身份标识，如果检测到请求的载体身份标识为某一款浏览器，说明该请求是个正常请求。但是如果检测到请求的载体身份标识不是基于某一款浏览器的，则为不正常请求，则服务器端很可能拒绝该次请求
#UA: User-Agent(请求载体的身份标识)
#UA伪装：让爬虫对应的请求载体身份标识伪装成某一款浏览器
import requests
import json
if __name__ == "__main__":
    #指定url
    url = "https://movie.douban.com/j/chart/top_list?"
    param = {
        'type': '24',
        'interval_id':'100:90',
        'action':'',
        'start':'0', #从库中第几部电影去取
        'limit':'20' #一次取出的个数
    }
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15(KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)'
    }
    #处理url携带的参数：封装到字典中
    #发起请求
    #get方法会返回一个响应对象
    response = requests.get(url=url,params=param,headers=headers)
    #获取响应数据 json方法返回的是一个obj（如果确认响应数据是json类型才可以）
    list_data = response.json()
    #持久化存储
    fp = open('./douban.json','w',encoding='utf-8')
    json.dump(list_data,fp=fp,ensure_ascii=False)
    print('Over！')