from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

ed = webdriver.Edge();
ed.maximize_window();
ed.implicitly_wait(10)
ed.get("http://www.baidu.com");

setting = WebDriverWait(ed,5,1).until(lambda ssss: ed.find_element("id","su"),message="no setting")
ed.find_element("id","kw").send_keys("god")
setting.click()
# 滚动
# js='window.scrollTo(0,500)'
# ed.execute_script(js)
time.sleep(3)
# 定位
el=ed.find_element(By.XPATH,'//*[@id="4"]/div/div/h3/a')
js='arguments[0].scrollIntoView()'
ed.execute_script(js,el)

time.sleep(3)

ed.quit()


