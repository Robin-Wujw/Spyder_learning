from selenium import webdriver 
from time import sleep
#滚动到浏览器顶部
js_top = "var q=document.documentElement.scrollTop=0"
  
#滚动到浏览器底部
js_bottom = "var q=document.documentElement.scrollTop=10000"
js_bottom2 = "window.scrollTo(0,document.body.scrollHeight)"

#页面放大
js_zoom_in = "document.body.style.zoom='1.7'"

#页面缩小
js_zoom_out = "document.body.style.zoom='0.5'"


driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get('https://www.baidu.com')
driver.execute_script(js_bottom)
sleep(1)
driver.execute_script(js_top)
sleep(1)
driver.execute_script(js_zoom_in)
sleep(1)
driver.execute_script(js_zoom_out)
sleep(1)
driver.close()