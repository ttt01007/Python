import pytest
import os
import allure

'''

'''


@pytest.fixture(scope='session')
def login_fixture():
    print('前置条件：登录 ')


@allure.step('步骤1')
def step_1():
    print('操作步骤-------------1')


@allure.step('步骤2')
def step_2():
    print('操作步骤-------------2')


@allure.step('步骤3')
def step_3():
    print('操作步骤-------------3')


@allure.epic('epic1,大特性')
@allure.feature('xx测试模块')
class TestDemoAllure():

    @allure.testcase('httpxxxx')
    @allure.issue('httpxxxx')
    @allure.title('用户标题')
    @allure.story('用户故事:1')
    @allure.severity('critical')
    def test_case_1(self, login_fixture):
        '''
            方法注释
            1.step1
            2.2
            3.3
        '''
        step_1()
        step_2()

    @allure.story('用户故事:2')
    def test_case_2(self, login_fixture):
        step_1()
        step_3()


@allure.epic('epic2,大特性')
@allure.feature('xxxxxxx测试模块')
class TestDemo2():

    @allure.story('用户故事:3')
    def test_case_3(self, login_fixture):
        step_1()
        step_3()

    @allure.story('用户故事:4')
    def test_case_4(self, login_fixture):
        step_1()
        step_3()


if __name__ == '__main__':
    pytest.main(['-s', 'test_case_01.py', '--alluredir', './result',
                 # 根据epic来执行
                 '--allure-epics=epic1,大特性',
                 # 根据feature执行
                 '--allure-features=xx测试模块',
                 # 根据story执行
                 '--allure-storys=用户故事:1',
                 '--clean-alluredir'])
    os.system('allure serve result')
