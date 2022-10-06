import unittest

'''
    1.如果要UnitTest生效，需要让自定义类直接继承unittest.TestCase
    2.UnitTest中测试用例都是以函数的形式存在，同时命名需要以test开头
    3.测试用例运行一定要在类中调用main，再在main中调用unittest.main()
        如果不写main方法，则类中会默认调用main方法，但是为了格式规范，一定要写
    4.在类中基于编译器可以单独运行测试用例，但是不需要，因为容易报错。
    5.如果我不以test开头命名，就是一个函数
    6.测试用例的执行顺序，是默认执行顺序，无法改变，根据test后面值得ASCII码排序
    7.在unittest中，用例执行后。默认是会强制关闭并结束进程。但是也会出现部分不清空的情况
        所以第一，不要考虑如何在用例执行后不关闭浏览器；第二，记得在用例末尾添加quit函数，以确保释放资源
    8.前置后置是固定写法，前置后置有且只有一个
    9.用例执行前都会运行一侧setup，执行后都会运行一次teardown
    10.所有的前置和后置不参与到实际的测试行为，只做初始化与资源释放的操作
    11.对于前置条件不同意的情况，用万能的setup和teardown
    12.自带断言:self.assert
'''
'''
    类执行顺序：
        1.main
        2.此城与Unitest.TestCase类的class
        3.setupClass(一个class对象只执行一次)
        4.setup(每个测试用例都执行一次)
        5.测试用例
        6.teardown(每个测试用例都执行一次)
        7.teardownCalss(一个class对象只执行一次)
'''


class UnitDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_01(self):
        print('01')
        self.tsw()

    def test_02(self):
        print('02')
        self.assertTrue(True, msg='真的')
        self.assertTrue(False, msg='假的')


    def tsw(self):
        print('TSW')


if __name__ == '__main__':
    unittest.main
