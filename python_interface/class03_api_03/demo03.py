import unittest

from Python.python_interface.class03_api_03.demo02 import ShowAPI


class TestExpress(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # cls.SECRET_ID = 'xxxxxx'
        # cls.SHOWAPI_APPID = 'xxxxxx'
        # cls.api = ShowAPI(cls.SHOWAPI_APPID, cls.SECRET_ID)
        cls.api = ShowAPI()
    def test_01(self):
        params = {'com': 'zhongtong', 'nu': 'xxxxxxxxx'}

        ret = self.api.send('post', '64-19', params)
        print(ret.text)
        self.assertEqual(ret.json()['showapi_res_code'], 0)


if __name__ == '__main__':
    unittest.main
