from time import sleep

# ʹ����conftest�г�ʼ�����˵�driver
import pytest


def test_baidu_case01(browser):
    driver = browser
    driver.get('http://www.baidu.com')
    sleep(1)
    driver.find_element('id', 'kw').send_keys('ggb')
    sleep(1)
    driver.find_element('id', 'su').click()
    sleep(1)
    assert driver.title == '11ggb_�ٶ�����'
