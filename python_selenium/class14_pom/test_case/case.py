import unittest

from selenium import webdriver

from python_selenium.class14_pom.page_object.login_page import LoginPage


class Case(unittest.TestCase):

    def test_find(self):
        driver = webdriver.Edge()
        find = LoginPage(driver)
        find.search('python')


if __name__ == '__main__':
    unittest.main()
