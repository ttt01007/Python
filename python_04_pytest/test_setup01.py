import pytest


def multiply(a, b):
    return a * b


# fixtures
'''
    第一批次:setup_class/teardown_class:在当前文件中,在所有测试用例执行之前与之后执行
    第二批次:setup_method/teardown_method:在每个测试函数之前与之后执行
    第三批次:setup/teardown:在每个测试函数之前与之后执行.这两个方法同样可以作用于类方法
    PS:执行顺序按批次顺序来,即使改变犯法位置,也是一样
'''


def setup_class(module):
    print("setup_module==============>")


def teardown_class(module):
    print("teardown_module===============>")


def setup_function(function):
    print("setup_function-------------->")


def teardown_function(function):
    print("teardown_function-------------->")


def setup():
    print("setup---->")

def teardown():
    print("teardown---->")


# =======测试用例========
def test_multiply_3_4():
    print('test_numbers_3_4')
    assert multiply(3, 4) == 12


def test_multiply_a_3():
    print('test_string_a_3')
    assert multiply('a', 3) == 'aaa'


if __name__ == '__main__':
    pytest.main(['-s', 'test_setup01.py'])
