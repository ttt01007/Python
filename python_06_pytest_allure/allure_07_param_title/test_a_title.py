import os
import pytest
import allure


def login(username, password):
    '''登录'''
    print('输入账号: %s' % username)
    print('输入账号: %s' % password)
    # 返回
    return {'code': 0, 'msg': 'success!'}


test_datas = [
    ({'username': 'zz1', 'password': '123456'}, 'success!'),
    ({'username': 'zz2', 'password': '111111'}, 'failed!'),
    ({'username': 'zz3', 'password': '333333'}, 'success!')
]

'''
    使用@allure.title时,可以加上传入的参数,
    如穿的参数test_input,expected 需要拼接test_input的值
'''
@allure.story('登录场景')
@allure.title('用例描述,测试输入:{test_input}{expected}')
@pytest.mark.parametrize('test_input, expected', test_datas,
                         ids=['输入正确账号,密码,登录成功',
                              '输入错误账号,密码,登录失败',
                              '输入正确账号,密码,登录成功'])
def test_login(test_input, expected):
    '''测试登录用例'''
    result = login(test_input['username'], test_input['password'])
    # 断言
    assert result['msg'] == expected


if __name__ == '__main__':
    # 不要家-s参数,allure将stdout输出到allure报告,加了指挥输出到consloe里
    # 用例执行步骤中会有一个stdout附件记录单个用例执行过程中的stdout
    pytest.main(['test_a_title.py','--alluredir', './result', '--clean-alluredir'])
    os.system('allure generate ./result/ -o ./report_allure/ --clean')
