import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    print('-------------------------------')

    # 获取常规钩子方法的调用结果，返回一个result对象
    out = yield
    print('用例执行结果', out)

    '''
        获取调用结果result的测试报告,返回一个report对象
        report对象的属性包括：
        when(setup,call,teardown三个值)、nodeid(测试用例的名字及所属
        文件和目录)
        outcome(用例的执行结果,passed,filed)
    '''
    report = out.get_result()
    print('测试报告: %s' % report)
    print('步骤 %s' % report.when)
    print('nodeid %s' % report.nodeid)
    print('description %s' % str(item.function.__doc__))
    print('运行结果 %s' % report.outcome)
