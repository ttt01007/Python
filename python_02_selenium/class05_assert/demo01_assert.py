from time import sleep

from selenium import webdriver

driver = webdriver.Edge()
# driver.maximize_window()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')
text = driver.find_element('xpath', '//*[@id="s-top-loginbtn"]').text
print('text:{}'.format(text))
assert text == '登录', '访问失败'
driver.close()

try:
    pass
except Exception as e:
    pass
finally:
    pass
