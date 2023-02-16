from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Edge()
# 窗口最大化
driver.maximize_window()
# 访问
driver.get('http://www.baidu.com')
# 点击
driver.find_element('', '').click()
# 输入，只有input标签可以输入,textarea也可以
driver.find_element('', '').send_keys('')
'''
    select下拉列表框：
        1.定位select元素
        2.转成select对象
        3.基于下标，value,text
'''
el = driver.find_element('name', 'select')
select = Select(el)
# 获取所有option内容
li = select.options
# 获取指定的值，进行传入
select.select_by_value('属性value的值')
select.select_by_index(1)
select.select_by_visible_text('文本内容')

driver.close()