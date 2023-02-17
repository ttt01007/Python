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


@allure.story('登录场景')
@pytest.mark.parametrize('test_input, expected', test_datas)
def test_login(test_input, expected):
    '''测试登录用例'''
    result = login(test_input['username'], test_input['password'])
    # 断言
    assert result['msg'] == expected


if __name__ == '__main__':
    # 不要家-s参数,allure将stdout输出到allure报告,加了指挥输出到consloe里
    # 用例执行步骤中会有一个stdout附件记录单个用例执行过程中的stdout
    pytest.main(['test_a.py','--alluredir', './result', '--clean-alluredir'])
    os.system('allure generate ./result/ -o ./report_allure/ --clean')
