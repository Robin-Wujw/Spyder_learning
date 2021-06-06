import selenium
import requests
from time import sleep
from selenium import webdriver
#实现无可视化界面
from selenium.webdriver.chrome.options import Options
#实现规避检测
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver import ActionChains
from eagle_demo import Chaojiying_Client
from PIL import Image

def getCodeText():
    chaojiying = Chaojiying_Client('635072437', 'wujiawei', '917557')	#用户中心>>软件ID 生成一个替换 96001
    im = open('code.png', 'rb').read()													#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    return chaojiying.PostPic(im, 9004)['pic_str']
#使用selenium打开登陆页面
option = Options()
#option.add_experimental_option('excludeSwitches',['enable-automation'])
option.add_argument('--disable-blink-features=AutomationControlled')
bro = webdriver.Chrome(executable_path='./chromedriver',options=option)
bro.maximize_window()

#无可视化界面(无头浏览器) phantomJS
bro.get('https://kyfw.12306.cn/otn/resources/login.html')
link_log = bro.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a')
sleep(0.5)
link_log.click()
sleep(0.5)
#截图
#确定验证码图片的左上角和右下角的坐标
code_img_ele = bro.find_element_by_xpath('//*[@id="J-loginImg"]')
code_img_ele.screenshot('code.png')
# location = code_img_ele.location #返回的是验证码图片左上角的坐标
# size = code_img_ele.size
# #左上角和右下角坐标
# rangle = int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height'])
# #至此验证码图片区域就确定下来了
# i = Image.open('./aa.png')
# code_img_name = './code.png'
# #crop根据指定区域进行图片裁剪
# frame = i.crop(rangle)
# frame.save(code_img_name)
result = getCodeText()
all_list = [] #要存储即将被点击的点的坐标 [[x1,y1],[x2,y2]]
if '|' in result:
    list_1 = result.split('|')
    count_1 = len(list_1)
    for i in range(count_1):
        xy_list = []
        x = int(list_1[i].split(',')[0])
        y = int(list_1[i].split(',')[1])
        xy_list.append(x)
        xy_list.append(y)
        all_list.append(xy_list)
else:
    x = int(result.split(',')[0])
    y = int(result.split(',')[1])
    xy_list = []
    xy_list.append(x)
    xy_list.append(y)
    all_list.append(xy_list)
#遍历列表，使用动作链对每一个列表元素对应的x,y指定的位置进行点击操作
for l in all_list:
    x = l[0]
    y = l[1]
    ActionChains(bro).move_to_element_with_offset(code_img_ele,x,y).click().perform()
bro.find_element_by_id('J-userName').send_keys('17671725832')
sleep(1)
bro.find_element_by_id('J-password').send_keys('wujiawei980729')
sleep(1)
bro.find_element_by_id('J-login').click()
sleep(0.5)
#如果程序被识别到了怎么办?
#1.chrome版本号小于88 在你启动浏览器的时候(此时没有加载任何网页内容)，向页面嵌入js代码 去掉webdriver
#web = Chrome()
# web.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",{
#     "source": """
#     window.navigator.webdriver = undefined
#         Object.defineProperty(navigator,'webdriver',{
#             get: () => undefined
#         })
#     """
# })
# web.get(xxxxxxx)
#2.chrome版本号大于88
# option = Options()
# #option.add_experimental_option('excludeSwitches',['enable-automation'])
# option.add_argument('--disable-blink-features=AutomationControlled')
# web = Chrome(options=option)
# web.get(xxxx)

#拖拽
btn = bro.find_element_by_xpath('//*[@id="nc_1_n1z"]')
ActionChains(bro).drag_and_drop_by_offset(btn,303,0).perform()

