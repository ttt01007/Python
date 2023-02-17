import os
import pytest
import allure
from Python.python_06_pytest_allure.allure_05_testcase_step.common_function import *

'''
    流程性得用例,添加测试步骤,让用例更清晰
    用例步骤：1.登陆， 2.浏览商品 3.添加购物车  4.生成订单  5.支付成功
'''
'''
    两种方式对比:
    使用with allure.step('step:步骤') 这种方式代码可读性更好一点
    但不会带上函数里面得传参和对应得值
    使用@allure.step('step:步骤')这种方式会带上函数得传参和对应的值
    这两种方式结合起来使用,才能更好的展示测试报告
'''


@pytest.fixture(scope='session')
def login_setup():
    with allure.step('setup:登录'):
        login('zz', '123456')


@allure.feature("功能模块")
@allure.story("测试用例小模块-成功案例")
@allure.title("测试用例名称：流程性的用例，添加测试步骤")
def test_add_goods_and_buy(login_setup):
    '''
    用例描述：
    前置：登陆
    用例步骤：1.浏览商品 2.添加购物车  3.购买  4.支付成功
    '''
    with allure.step("step1：浏览商品"):
        open_goods()

    with allure.step("step2：添加购物车"):
        add_shopping_cart()

    with allure.step("step3：生成订单"):
        buy_goods()

    with allure.step("step4：支付"):
        pay_goods()

    with allure.step("断言"):
        assert 1 == 1


if __name__ == '__main__':
    pytest.main(['-s', 'test_allure_step.py', '--alluredir', './result',
                 '--clean-alluredir'])
    os.system('allure serve result')
