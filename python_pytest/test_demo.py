import pytest

'''
    1.pytest将在当前目录及其子目录中运行所有格式为test_*或者*_test.py文件
    2.测试方法/函数默认必须事test开头的
    3.测试类必须事Test
'''
'''
    如果未指定参数，则集合从testpaths（如果已配置）或当前目录开始。
    或者，命令行参数 可用于目录、文件名或节点 ID 的任意组合。
    递归到目录中，除非它们与 norecursedirs 匹配。
    在这些目录中，搜索 或 按其测试包名称导入的文件。test_*.py*_test.py
    从这些文件中收集测试项：
        test类外的带前缀的测试函数或方法。
        test带前缀的测试类中的带前缀的测试函数或方法（无方法）。还考虑了装饰的方法。
        Test__init__@staticmethod@classmethods
'''


def test_01():
    print('test_01')
    assert 1 == 1


# @pytest.mark.smoke
# def test_02():
#     print('smoke:test_02')


def test_03():
    print('test_03')
    assert 1 == 2


if __name__ == '__main__':
    '''
    -s 输出print内容
    -v 显示具体得详细信息
    '-k','kkk' 执行方法名包括kkk得用例
    -q 最简化信息输出
    -x 如果出现失败用例，则退出测试
    --ignore=pathpytest 忽略执行的匹配路径
    
    '''
    # pytest.main(['-s'])
    # 生成junit XML测试报告
    # pytest.main(['-s', '--junit-xml=./report/log01.xml'])
    # 指定执行文件和具体方法
    # pytest.main(['-s', './python_test01/test_demo.py::test_02'])#指定执行文件和具体方法
    # 忽略执行的匹配路径
    # pytest.main(['-s','--ignore=python_test01'])
    # 用例失败控制,失败2此，结束测试
    # pytest.main(['-s', '--maxfail=2'])
    # 执行被装饰器@pytest.mark.show 装饰的所有测试用例,
    # 配合pytest.ini中
    # markers =
    #     smoke: desc
    # pytest.main(['-s', '-m', 'smoke', './test_demo.py'])
    # 执行未标记的测试用例，加上not
    # pytest.main(['-s', '-m', 'not smoke', './test_demo.py'])
    # 多线程执行测试
    # pip install pytest-xdist
    # pytest.main(['-n', '2', './test_demo.py'])
    # 重新运行失败用例
    # pip install pytest-rerunfailures
    # pytest-rerunfailures是一个可以使pytest重新运行测试得插件，以消除间歇性故障。
    # pytest.main(['--reruns', '5', './test_demo.py'])
    # 添加每次重跑之间得时间间隔
    # pytest.main(['--reruns', '5', '--reruns-delay', '1', './test_demo.py'])
