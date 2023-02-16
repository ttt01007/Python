'''
    1.强制等待
    2.隐式等待
    3.显式等待
'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

ed = webdriver.Edge()
ed.maximize_window()
# 隐式等待
ed.implicitly_wait(10)

ed.get("https://music.163.com/")
# 显式等待
WebDriverWait(ed, 5, 0.5).until(lambda el1: ed.find_element(By.LINK_TEXT, "登录"), message="登录没找到").click()
# el=WebDriverWait(ed,5,0.5).until(ed.find_element(By.LINK_TEXT,"登录"),message="登录没找到")

# ed.find_element(By.LINK_TEXT,"登录").click()
# ed.find_element(By.XPATH, "//a[text()='登录']").click();
time.sleep(3)

'''
    弹窗
        1.alert：确认
        2.prompt：支持输入并确认
        3.confirm：确认与取消
'''
# alert弹窗
alert = ed.switch_to.alert
alert.accept()
# confirm弹窗处理
alert.dismiss()
alert.accept()
# prompt
alert.send_keys('13123123')
alert.accept()
alert.dismiss()




ed.close()
