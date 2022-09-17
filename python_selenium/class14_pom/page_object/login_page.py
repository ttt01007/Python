from selenium import webdriver

from python_selenium.class14_pom.base_page.base_page import WebKeys


class LoginPage(WebKeys):
    url = 'http://www.baidu.com'

    textfind = ('id', 'kw')
    buttonclick = ('id', 'su')

    def search(self, text):
        self.visit(self.url)
        self.input(self.textfind, text)
        self.click(self.buttonclick)
        self.sleep(5)
        self.quit()


if __name__ == '__main__':
    driver = webdriver.Edge()
    text = 'python'
    LoginPage(driver).search(text)
