from time import sleep

# 使用在conftest中初始化好了的driver
import pytest


def test_baidu_case01(browser):
    '''
    注释111111
    '''
    driver = browser
    driver.get('http://www.baidu.com')
    sleep(1)
    driver.find_element('id', 'kw').send_keys('ggb')
    sleep(1)
    driver.find_element('id', 'su').click()
    sleep(1)
    assert driver.title == '11ggb_百度搜索'
