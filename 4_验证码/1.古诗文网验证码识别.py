from typing import DefaultDict
import requests
from lxml import etree
from  eagle_demo  import Chaojiying_Client 
def getCodeText():
    chaojiying = Chaojiying_Client('635072437', 'wujiawei', '917557')	#用户中心>>软件ID 生成一个替换 96001
    im = open('code.jpg', 'rb').read()													#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    return chaojiying.PostPic(im, 1902)			
#将验证码图片下载到本地
url = "https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx"
headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15(KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)'
}
page_text = requests.get(url=url,headers=headers).text 
#解析验证码图片img标签中src属性值
tree = etree.HTML(page_text)
code_img_src = 'https://so.gushiwen.cn'+tree.xpath('//*[@id="imgCode"]/@src')[0]
img_data = requests.get(url=code_img_src,headers=headers).content 
#将验证码图片保存到本地
with open('./code.jpg','wb') as fp:
    fp.write(img_data)
#调用打码平台的实例程序进行验证码图片数据识别
getCodeText()['pic_str']