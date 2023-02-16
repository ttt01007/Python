from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
import logging.config

from python_selenium.class09_ui_frame.my_conf import log_conf
from python_selenium.class09_ui_frame.my_conf.demo02_edge_options import Options


def open_browser(type_):
    try:
        driver = getattr(webdriver, type_)(options=Options().conf_options())
    except Exception as e:
        print(e)
        driver = webdriver.Edge(options=Options().conf_options())
    return driver


class WebKeys:
    # log = log_conf.get_log('../my_conf/log.ini')
    def __init__(self, type_, log):
        self.driver = open_browser(type_)
        self.log = log
        self.driver.implicitly_wait(10)

    def visit(self, text):
        self.driver.get(text)

    def quit(self):
        self.driver.quit()

    def locator(self, name, value):
        return self.driver.find_element(name, value)

    def input(self, name, value, text):
        self.locator(name, value).send_keys(text)

    def click(self, name, value):
        self.locator(name, value).click()

    def sleep(self, text):
        time.sleep(text)

    def wait(self, name, value):
        WebDriverWait(self.driver, 10, 0.5).until(lambda e1: self.locator(name, value), '等待失败')

    def assert_text(self, name, value, text):
        try:
            assert text == self.locator(name, value).text, '断言失败:{}'.format(text)
            return True
        except Exception as e:
            # logging.error(e)
            self.log.error(e)
            return False
