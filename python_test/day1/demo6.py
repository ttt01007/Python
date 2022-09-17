from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

ed = webdriver.Edge();
ed.maximize_window();
ed.implicitly_wait(10)
ed.get("https://www.taobao.com/");
# ed.find_element(By.ID,"s-usersetting-top").click()
setting = WebDriverWait(ed,5,1).until(lambda ssss: ed.find_element(By.XPATH, '//*[@id="J_SiteNavBdL"]/li[1]/div[1]/span[1]'),message="no setting")
setting.click()
time.sleep(3)

ed.quit()