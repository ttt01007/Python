'''
    UnitTest中的ddt数据驱动应用
        环境部署：
            pip install ddt
        ddt模块所有的内容都是基于装饰器的形态来实现补充的。
        一定要在调用ddt的类中声明ddt的调用，也就是在class前面加入@ddt
        在需要调用数据驱动的用例前，调用@data，实现数据的驱动分离
        file_data用于处理yaml格式的文件
        yaml格式的数据驱动管理时一个yaml对应一条用例
'''
import unittest
from ddt import ddt, file_data, data, unpack
from python_test.excel.excel_driver.web_keys import WebKeys


def read_file():
    li = []
    file = open('data/1.txt', 'r', encoding='utf-8')
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

    '''
        data执行的操作就是拆包
            @data('111','222','333')
            将所有数据进行分割:
                111
                222
                333
            基于拆分出来的结果总数,定义循环次数,每次循环都传入一个参数进去
        当需要传入多个参数的时候,所以需要二次解包
    '''

    # @data('python', 'mandy')
    # # data传入数据，多个参数传入元组,或者数列，或者字典，unpack解包元组按顺序传入
    # def test_01(self, text):
    #     self.wk.visit('http://www.baidu.com')
    #     self.wk.input('id', 'kw', text)
    #     self.wk.click('id', 'su')
    #     self.wk.sleep(3)
    #
    # @data(('python', 'su'), ('java', 'su'))
    # @unpack
    # # data传入数据，多个参数传入元组,或者数列，或者字典，unpack解包元组按顺序传入
    # def test_02(self, text, ttt):
    #     self.wk.visit('http://www.baidu.com')
    #     self.wk.input('id', 'kw', text)
    #     self.wk.click('id', ttt)
    #     self.wk.sleep(3)
    #
    # 基于文件的内容度,实现数据驱动
    # @data(*read_file())
    # def test_02(self, name):
    #     print(name)
    #
    #
    @file_data('./data/test_data.yaml')
    def test_03(self, **kwargs):
        self.wk.visit(kwargs['url'])
        self.wk.input(**kwargs['input'])
        self.wk.click(**kwargs['click'])
        self.wk.sleep(3)




if __name__ == '__main__':
    unittest.main
