import pytest
import os
import allure

'''
    allure对用例的等级划分成五个等级:
    blocker 阻塞缺陷(功能未实现,无法下一步)
    critical 严重缺陷(功能点缺失)
    normal 一般缺陷(边界情况,格式错误)
    minor 次要缺陷(界面错误与ui需求不符)
    trivial 轻微缺陷(必须项物体时,或者提示不规范
'''


@allure.severity('blocker')
def test_case_1():
    '''
        操作:test_case_1
    '''
    print('test_case_1')


@allure.severity('critical')
def test_case_2():
    '''
        操作:test_case_2
    '''
    print('test_case_2')


@allure.severity('normal')
def test_case_3():
    '''
        操作:test_case_3
    '''
    print('test_case_3')


@allure.severity('minor')
def test_case_4():
    '''
        操作:test_case_4
    '''
    print('test_case_4')


@allure.severity('trivial')
def test_case_5():
    '''
        操作:test_case_5
    '''
    print('test_case_5')


if __name__ == '__main__':
    pytest.main(['-s', 'test_case_01.py', '--alluredir', './result',
                 '--allure-severities', 'blocker,critical',
                 '--clean-alluredir'])
    os.system('allure serve result')
