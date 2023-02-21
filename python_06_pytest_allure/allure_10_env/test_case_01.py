# allure报告默认没有环境信息
# 添加环境信息方式一：result目录下添加environment.properties 添加到allure的报告数据目录，result下
# 不支持中文
import os
import pytest
import allure
data = [
    ("name1", "123456", "name1 登录成功"),
    ("name2", "123456", "name2 登录失败"),
    ("name3", "123456", "name3 登录成功")
]


def test_1():
    """
    动态设置描述
    """
    print(123)
    allure.dynamic.description("动态描述")
    allure.dynamic.title("动态标题")


@pytest.mark.parametrize('username,pwd,title', data)
def test_2(username, pwd, title):
    """
    登录测试用例1
    """
    print(username, pwd)
    allure.dynamic.title(title)


if __name__ == '__main__':
    pytest.main(['test_case_01.py', '--alluredir', './result'])
    # 自动生成本地可以访问的服务,不会生成报告文件
    os.system('allure serve result')
