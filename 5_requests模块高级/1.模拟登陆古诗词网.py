import requests
from lxml import etree 
from eagle_demo import Chaojiying_Client
#编码流程:
#1.验证码识别,获取验证码图片的文字数据
#2.对post请求进行发送(处理请求参数)
#3.对响应数据进行持久化存储
def getCodeText():
    chaojiying = Chaojiying_Client('635072437', 'wujiawei', '917557')	#用户中心>>软件ID 生成一个替换 96001
    im = open('code.jpg', 'rb').read()													#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    return chaojiying.PostPic(im, 1902)	
#1.对验证码图片进行捕获和识别
url = "https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15(KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)'
}
#创建一个session对象
session = requests.session()
page_text = session.get(url=url,headers=headers).text
tree = etree.HTML(page_text)
code_img_src = 'https://so.gushiwen.cn'+tree.xpath('//*[@id="imgCode"]/@src')[0]
img_data = session.get(url=code_img_src,headers=headers).content 
#将验证码图片保存到本地
with open('./code.jpg','wb') as fp:
    fp.write(img_data)
#调用打码平台的实例程序进行验证码图片数据识别
result = str(getCodeText()['pic_str'])
print(result)
print(type(result))
#post请求的发送(模拟登陆)
login_url = "https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx"
data = {
    'email': '17671725832',
    'pwd': 'wujiawei',
    'code': result,
    'denglu': '登录'
}
resp = session.post(url=login_url,headers=headers,data=data)
#打印响应状态码 200即为成功
print(resp.status_code)
#爬取当前用户个人主页对应的页面数据
detail_url = 'https://so.gushiwen.cn/user/collect.aspx'
#使用携带cookies的session进行get请求发送
detail_page_text = session.get(url=detail_url,headers=headers).text 
with open('robin.html','w',encoding='utf-8') as fp:
    fp.write(detail_page_text)