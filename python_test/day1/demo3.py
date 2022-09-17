from selenium import webdriver
from selenium.webdriver.remote.command import Command
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Edge(executable_path="msedgedriver")
# driver.get("http://www.baidu.com")
driver.execute(Command.GET, {'url': "http://www.baidu.com"})
driver.find_element("id", "kw").send_keys("selenium")
# driver.find_element("id","kw")._execute("sendKeysToElement",{"text":"selenium","value":""})
driver.find_element("id", "su").click()
time.sleep(3)
driver.quit()

wh = driver.window_handles
driver.switch_to.window(wh[1])
driver.switch_to.frame("id")
driver.switch_to.default_content()
