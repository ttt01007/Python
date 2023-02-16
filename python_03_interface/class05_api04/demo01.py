import configparser
import os
import unittest

from Python.python_03_interface.class03_api_03.demo01 import HttpClient


class TestAPIDemo(unittest.TestCase):
    httpclient = None
    url = None

    @classmethod
    def setUpClass(cls) -> None:
        TestAPIDemo.httpclient = HttpClient()
        config = configparser.ConfigParser()
        config_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'class03_api_03')
        print(config_dir)
        config.read(config_dir + '\env.ini', encoding='utf-8')
        TestAPIDemo.url = config.get('apidemo01', 'URL')
        print(TestAPIDemo.url)

    def test_01_login(self):
        path = None
        url = self.url + path
        method = 'post'
        data = {'password': '123456', 'username': 'admin'}

        ret = TestAPIDemo.httpclient(method=method, url=url, params_type='json', data=data)
        print(ret.text)


if __name__ == '__main__':
    unittest.main()
