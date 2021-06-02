# 如何使用
# - 指定url
# - 发起请求
# - 获取响应数据
# - 持久化存储
#爬取国家药品监督总局化妆品生产许可相应数据
  # 动态加载数据
  # 首页中对应的企业信息数据是通过ajax动态请求到的
#UA检测：门户网站的服务器会检测对应请求的载体身份标识，如果检测到请求的载体身份标识为某一款浏览器，说明该请求是个正常请求。但是如果检测到请求的载体身份标识不是基于某一款浏览器的，则为不正常请求，则服务器端很可能拒绝该次请求
#UA: User-Agent(请求载体的身份标识)
#UA伪装：让爬虫对应的请求载体身份标识伪装成某一款浏览器
#http://scxk.nmpa.gov.cn:81/xk/itownet/portal/dzpz.jsp?id=d99457a4d1504b1483ea2bc46666a0aa
# 通过对详情页url的观察 发现url的域名都是一样的 只有携带的参数id不一样
# id可以从首页对应的ajax请求得到的json串获取
# 域名和id拼接一个完整的企业对应的详情页的url
# 详情页的企业详情数据也是动态加载出来的 
# ajax-url：
# http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById
# http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById
# 观察后发现所有post请求url都是一样的 只有参数id不同 
# 如果我们可以批量获取多家企业的id后 就可以将id和url形成一个完整的详情页对应详情数据的ajax请求url
import requests
import json
if __name__ == "__main__":
    #指定url
    url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList"
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15(KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)'
    }
    id_list =  []
    all_data_list = [] #存储所有企业详情数据
    #参数的封装
    for page in range(1,6):
        page = str(page)
        data = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn':''
        }
        json_ids = requests.post(url=url,data=data,headers=headers).json()
        #获取响应数据 json方法返回的是一个obj（如果确认响应数据是json类型才可以）
        for dic in json_ids['list']:
            id_list.append(dic['ID'])

    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        data = {
            'id': id 
        }
        detail_json = requests.post(url=post_url,headers=headers,data=data).json()
        all_data_list.append(detail_json)
    #持久化存储
    fp = open('./allData.json','w',encoding='utf-8')
    json.dump(all_data_list,fp=fp,ensure_ascii=False)
    print('over!')