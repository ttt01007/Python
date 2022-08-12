# 装饰器
import unittest
from ddt import ddt, data, unpack, file_data
from excel.excel_driver.web_keys import WebKeys


def read_file():
    li = []
    file = open('./data/1.txt', 'r', encoding='utf-8')
    for line in file.readlines():
        li.append(line)
    file.close()
    return li


@ddt  # 声明该class将要调用ddt模块进行数据管理
class UnitDemo(unittest.TestCase):
    def setUp(self) -> None:
        self.wk = WebKeys('Edge')

    def tearDown(self) -> None:
        self.wk.quit()

    # @data(('python', 'su'), ('java', 'su'))
    # @unpack
    # # data传入数据，多个参数传入元组,或者数列，或者字典，unpack解包元组按顺序传入
    # def test_01(self, text, ttt):
    #     self.wk.visit('http://www.baidu.com')
    #     self.wk.input('id', 'kw', text)
    #     self.wk.click('id', ttt)
    #     self.wk.sleep(3)


    @file_data('./data/test_data.yaml')
    def test_01(self, **kwargs):
        self.wk.visit(kwargs['url'])
        self.wk.input(**kwargs['input'])
        self.wk.click(**kwargs['click'])
        self.wk.sleep(3)


    # @data(*read_file())
    # def test_02(self, name):
    #     print(name)


if __name__ == '__main__':
    unittest.main
