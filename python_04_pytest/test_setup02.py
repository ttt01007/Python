import pytest


def multiply(a, b):
    return a * b


# fixtures
class TestMultiply:
    '''
        第一批次:setup_module/teardown_module:在当前文件中,在所有测试用例执行之前与之后执行
        第二批次:setup_function/teardown_function:在每个测试函数之前与之后执行
        第三批次:setup/teardown:在每个测试函数之前与之后执行.这两个方法同样可以作用于类方法
        PS:执行顺序按批次顺序来,即使改变犯法位置,也是一样
    '''

    @classmethod
    def setup_class(cls):
        print("setup_class==============>")

    @classmethod
    def teardown_class(cls):
        print("teardown_class===============>")

    def setup_method(self, method):
        print("setup_method-------------->")

    def teardown_method(self, method):
        print("teardown_method-------------->")

    def setup(self):
        print("setup---->")
        assert 1 == 2

    def teardown(self):
        print("teardown---->")

    # =======测试用例========
    def test_multiply_3_4(self):
        print('test_numbers_3_4')
        assert multiply(3, 4) == 12

    def test_multiply_a_3(self):
        print('test_string_a_3')
        assert multiply('a', 3) == 'aaa'


if __name__ == '__main__':
    pytest.main(['-s', 'test_setup02.py'])
