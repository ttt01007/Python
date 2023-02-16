# 装饰器
import unittest


class UnitDemo(unittest.TestCase):
    flag = 0
    # 无条件跳过
    @unittest.skip('无条件跳过')
    def test_01(self):
        print('01')

    @unittest.skipIf(1 == 1, '判断为true，跳过')
    def test_02(self):
        print('02')

    @unittest.skipUnless(1 == 2, '与skipif相反')
    def test_03(self):
        print('03')

    # 报错了就跳过
    @unittest.expectedFailure
    def test_04(self):
        print('04')
        a = (1, 2)
        a[0] = 2

    def test_05(self):
        print('05')


if __name__ == '__main__':
    unittest.main
