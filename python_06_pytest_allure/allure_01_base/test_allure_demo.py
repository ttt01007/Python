import os

import pytest
import allure


@allure.step('步骤1：点击搜索框')
def step_1():
    print('111')


@allure.step('步骤2：点击下拉框')
def step_2():
    print('222')


@allure.feature('编辑页面')
class TestEdiePage():
    '''编辑页面'''

    @allure.story('这是一个xx用户故事的场景用例')
    def test_1(self, login):
        '''用例描述：先登录，再执行步骤step1，step2'''
        step_1()
        step_2()
        print('xxx')

    @allure.story('这是一个yy用户故事的场景用例')
    def test_2(self, login):
        '''用例描述：先登录'''
        print('yyy')


if __name__ == '__main__':
    pytest.main(['-s', 'test_allure_demo.py', '--alluredir', './result'])
    os.system('allure serve result')
