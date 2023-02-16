from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait

ed = webdriver.Edge()
# 等待页面10秒内完全加载
ed.implicitly_wait(10)
ed.maximize_window()
ed.get("https://music.163.com/")
WebDriverWait(ed, 5, 0.5).until(lambda el1: ed.find_element(By.LINK_TEXT, "登录"), message="登录没找到").click()
# el=WebDriverWait(ed,5,0.5).until(ed.find_element(By.LINK_TEXT,"登录"),message="登录没找到")

# ed.find_element(By.LINK_TEXT,"登录").click()
# ed.find_element(By.XPATH, "//a[text()='登录']").click();
time.sleep(3)
ed.find_element(By.XPATH, "//a[text()='选择其他登录模式']").click();
# el=WebDriverWait(ed,5,1).until(lambda el1: ed.find_element(By.ID, "j-official-terms"),message="协议勾选没找到")
ed.find_element(By.ID, "j-official-terms").click();
time.sleep(3)
ed.find_element(By.XPATH, "//a[text()='QQ登录']").click();
time.sleep(3)
# 获取所有句柄
wh = ed.window_handles
print(wh)
print(ed.title)
ed.close()
# 选择句柄
ed.switch_to.window(wh[1])
print(ed.title)
# 切换内嵌的html，iframe，参数是id或者name，没有id可以传入元素
# frame = ed.find_element('id', 'ptlogin_iframe')
# ed.switch_to.frame(frame)
ed.switch_to.frame("ptlogin_iframe")
ed.find_element(By.LINK_TEXT, "密码登录").click()
# ed.find_element(By.XPATH, "//a[text()='密码登录']").click();
time.sleep(3)
ed.find_element(By.ID, "u").send_keys("398847378")
ed.find_element(By.ID, "p").send_keys("201016016123")
time.sleep(3)
# ed.find_element(By.XPATH,"//*[text()='登录']")
ed.find_element(By.XPATH, "//input[@value='登录']").click()
time.sleep(3)
# 句柄使用以后切换回来
# ed.switch_to.default_content()
# ed.close()
