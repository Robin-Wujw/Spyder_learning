from selenium import webdriver 
#导入动作链对应的类
from selenium.webdriver import ActionChains
from lxml import etree
import time 
#实例化一个浏览器对象(传入浏览器的驱动程序)
bro = webdriver.Chrome(executable_path='./chromedriver')
bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
time.sleep(2)
#如果定位的标签存在于iframe标签之中的，则必须通过如下操作进行标签定位
bro.switch_to.frame("iframeResult")#切换浏览器标签定位的作用域
div = bro.find_element_by_id("draggable")

#动作链实现拖动
action =ActionChains(bro)
#点击长按指定的标签
action.click_and_hold(div)

for i in range(5):
    action.move_by_offset(17,0).perform()
    time.sleep(0.3)
#释放动作链
action.release()
bro.close()