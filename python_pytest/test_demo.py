import pytest

'''
    pytest将在当前目录及其子目录中运行所有格式为test_*或者*_test.py文件
'''


def test_01():
    print('test_01')
    assert 1 == 1


if __name__ == '__main__':
    '''
    -s 输出print内容
    -v 显示具体得详细信息
    '-k','kkk' 执行方法名包括kkk得用例
    -q 最简化信息输出
    -x 如果出现失败用例，则退出测试
    '''
    pytest.main(['-q', '--junit-xml=./report/log01.xml'])
    # -s可以输出print内容 -v 显示具体得详细信息
    # pytest.main(['-s', './python_test01/test_demo.py::test_02'])#指定执行文件和具体方法
    # pytest.main(['-s','--ignore=python_test01'])
