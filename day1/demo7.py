import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

ed = webdriver.Edge()
ed.get('https://www.baidu.com')
ed.maximize_window()
ed.implicitly_wait(10)

span=WebDriverWait(ed,5,1).until(lambda e1:ed.find_element(By.XPATH,'//*[@id="form"]/span[1]/span[1]'),message="没找到等待元素")
span.click()
inputmange=ed.find_element(By.XPATH,'//*[@id="form"]/div/div[2]/div[2]/input')
inputmange.send_keys(r'C:\Users\39884\Desktop\微信图片_20220728134709.jpg')
time.sleep(5)
ed.quit()