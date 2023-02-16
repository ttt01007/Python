from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('http://www.baidu.com')

driver.find_element(By.ID, 'kw').send_keys('python')

driver.find_element(By.ID, 'su').click()

sleep(3)

driver.close()
