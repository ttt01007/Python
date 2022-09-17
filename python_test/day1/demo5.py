from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

# assert True, "1";
ed = webdriver.Edge()
ed.maximize_window()
ed.implicitly_wait(10)
ed.get("http://www.baidu.com")
# time.sleep(3)
setting = WebDriverWait(ed,5,1).until(lambda ssss: ed.find_element(By.ID, "s-usersetting-top"),message="no setting")
action = ActionChains(ed)
action.move_to_element(setting).perform()
time.sleep(5)
ed.close()
