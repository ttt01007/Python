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
    ({'username': 'zz6', 'password': '123456'}, 'success!'),
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
    # allure报告可以记录用例每次执行的情况,方便跟踪用例的成功率,数据保留到json文件中
    # 会带来一个问题,当你代码里面的用例删除,或者更换名称后,依然会记录之前的用例报告
    # --clean-alluredir 每次用例执行之前先清空allure的报告记录
    # pytest.main(['test_a.py', '--alluredir', './result'])
    pytest.main(['test_a.py', '--alluredir', './result', '--clean-alluredir'])
    # 自动生成本地可以访问的服务,不会生成报告文件
    os.system('allure serve result')
    # 生成报告文件到工程里
    # os.system('allure generate ./result/ -o ./report_allure/ --clean')
    # 这里的clean,只是让报告可以重新生成,生成的结果,依然会保留之前用例执行的记录
    # json文件每次执行都会不断增加,不加--clean,只能生成一次,然后提示无法生成报告
