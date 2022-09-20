from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.webdriver import WebDriver

# driver = webdriver.Edge()
driver = WebDriver()
#
# driver.get('http://www.baidu.com')
driver.execute('get', {'url': 'http://www.baidu.com'})
#
# driver.find_element(By.ID, 'kw').send_keys('python')
el1 = driver.execute('findElement', {
    'using': 'xpath',
    'value': '//input[@id="kw"]'})['value']

el1._execute('sendKeysToElement', {
    'text': 'python',
    'value': ''
})
# driver.find_element(By.ID, 'su').click()
el2 = driver.find_element(By.ID, 'su')
el2._execute('clickElement')
#
sleep(5)
#
# driver.close()
driver.execute('close')
