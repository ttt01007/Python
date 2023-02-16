import pytest
import os
import allure

'''
    [自动化用例]
    feature 特性名称
    story 用户故事/场景
    title 对应用例的标题
    testcase 对应禅道系统的bug用例url地址,关联起来
    issue 如果这个用例有bug,应该关联对应的bug地址
    step 用例步骤描述
    功能用例整体描述:写在用例方法的注释里
'''


@allure.feature('编辑分类文章')
class TestArticleClassify():
    @allure.story('典型场景')
    @allure.title('登录-编辑文章分类,重复保存,保存失败')
    @allure.issue('http')  # 禅道bug地址
    @allure.testcase('http')  # 禅道用例链接地址
    def test_edit_classify(self):
        '''
            用例描述:登录-编辑文章分类,重复保存,保存失败
            0.登录
            1.编辑文章分类，输入文章类别，如计算机
            2.点击保存按钮
            3.重新打开编辑页面，输入：计算机
            4.再次点击保存按钮
            assert:保存失败,提示:已存在
        '''
        with allure.step('setup0:登录login'):
            print('登录')
            assert 1 == 1
        with allure.step('setup1:编辑文章分类，输入文章类别，如计算机'):
            print('step1')
            assert 1 == 1
        with allure.step('setup2:点击保存按钮'):
            print('step2')
            assert 1 == 1
        with allure.step('setup3:重新打开编辑页面，输入：计算机'):
            print('step3')
            assert 1 == 1
        with allure.step('setup4:再次点击保存按钮'):
            print('step4')
            assert 1 == 1
        with allure.step('assert:保存失败,提示:已存在'):
            print('assert')
            assert 1 == 1


if __name__ == '__main__':
    pytest.main(['-s', 'test_case_01.py', '--alluredir', './result'])
    os.system('allure serve result')
