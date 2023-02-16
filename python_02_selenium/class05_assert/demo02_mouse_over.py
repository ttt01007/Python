'''
    鼠标悬停：通过ActionChains类来实现悬停的才做行为
'''
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')
el = driver.find_element('xpath', '//span[text()="设置"]')
actions = ActionChains(driver)
actions.move_to_element(el).perform()
sleep(3)
driver.close()
