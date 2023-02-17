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
    ({'username': 'zz1', 'password': '123456'}, 'success!', '输入正确账号,密码,登录成功'),
    ({'username': 'zz2', 'password': '111111'}, 'failed!', '输入错误账号,密码,登录失败'),
    ({'username': 'zz3', 'password': '333333'}, 'success!', '输入正确账号,密码,登录成功')
]

'''
    结合到上面面的ids和title实现方式,把用例描述当成一个测试输入的参数,继续优化
    parametrize 里面三个参数 test_input,expected,title 和
    test_login(test_input, expected, title) 里面参数保持一致
'''


@allure.story('登录场景')
@allure.title('{title}')
@pytest.mark.parametrize('test_input, expected, title', test_datas
                         )
def test_login(test_input, expected, title):
    '''测试登录用例'''
    result = login(test_input['username'], test_input['password'])
    # 断言
    assert result['msg'] == expected


if __name__ == '__main__':
    # 不要家-s参数,allure将stdout输出到allure报告,加了指挥输出到consloe里
    # 用例执行步骤中会有一个stdout附件记录单个用例执行过程中的stdout
    pytest.main(['test_a_title_new.py', '--alluredir', './result', '--clean-alluredir'])
    os.system('allure generate ./result/ -o ./report_allure/ --clean')
