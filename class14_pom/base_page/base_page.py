import time

from selenium.webdriver.support.wait import WebDriverWait


class WebKeys:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def visit(self, text):
        self.driver.get(text)

    def quit(self):
        self.driver.quit()

    def locator(self, loc):
        return self.driver.find_element(*loc)

    def input(self, loc, text):
        self.locator(loc).send_keys(text)

    def click(self, loc):
        self.locator(loc).click()

    def sleep(self, text):
        time.sleep(int(text))

    def wait(self, loc):
        WebDriverWait(self.driver, 10, 0.5).until(lambda e1: self.locator(*loc), '等待失败')

    def assert_text(self, loc, text):
        try:
            assert text == self.locator(loc).text, '断言失败'
            return True
        except:
            return False
