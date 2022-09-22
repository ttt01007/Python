'''
    Document 对象，特殊场景用
    作用：
        1.定位元素
        2.通过Document修改元素属性，添加或者移除
        3.滚动条操作
            0:最上面
            500：中间
            1000：最下面
        4.滚动到指定元素
            操作滚动条的目的就是为了将指定的元素显示出来，能通过selenium进行定位操作
            arguments[0]相当于占位符
            通过js获取对象或者内容时，需要添加return
'''
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get('http://www.baidu.com')

driver.find_element(By.ID, 'kw').send_keys('python')

driver.find_element(By.ID, 'su').click()

sleep(3)
# 滚动条操作
driver.find_element('xpath', '//*[contains(text(),"python")]')
js = 'window.scrollTo(0,500)'
# 通过js执行器来实现js语句的调用
driver.execute_script(js)
sleep(5)

# 滚动到指定元素
el = driver.find_element('xpath', '//*[contains(text(),"python")]')
js = 'arguments[0].scrollIntoView()'
driver.execute_script(js, el)
sleep(5)

# 删除指定属性 removeAttribute("name")
el = driver.find_element('xpath', '//*[contains(text(),"python")]')
js = 'arguments[0].removeAttribute("name")'
driver.execute_script(js, el)
sleep(5)

# 获取文本 通过js获取对象或者内容时，需要添加return
el = driver.find_element('xpath', '//*[contains(text(),"python")]')
js = 'return arguments[0].innerHTML'
text = driver.execute_script(js, el)
print(text)
sleep(5)

driver.close()
