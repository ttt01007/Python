# 元素定位
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get('http://www.baidu.com')
# id定位
driver.find_element('id', 'kw')
# name定位
driver.find_element('name', 'kw')
# 通过 link text （a标签）进行元素定位，根据文本进行查找
driver.find_element('link text', '新闻')
# 通过partial link text 定位，根据文本进行查找
driver.find_element('partial link text', '新闻')
# 通过标签来定位 tag name
driver.find_element('tag name', 'a')  # input li
# 通过classname定位,不推荐
driver.find_element('class name', '')
# 通过css selector定位 #代表id
driver.find_element('css selector', '#kw')
# 通过xpath 定位，万金油
# 绝对路径：/html/body/div[1]/div[1]/div[5]/div/div/form/span[2]/input
# 相对路径：//input[@id="su" and @id="su"]
# 基本语法规则：
# // 从根路径查找
# input 查找标签
# [] 添加筛选条件
# @ 表示属性（Attribute）
# and 也通过条件
# //input[@id="su"]/.. 查找父元素
# //input[text()='新闻']
# //*[contains(text(),'新')] 将所有包含新的元素查找出来
