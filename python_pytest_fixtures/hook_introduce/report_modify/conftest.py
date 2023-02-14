from datetime import datetime
from py.xml import html
import pytest

'''
    sortable time 可排序的
    cells.pop() 最后一列删掉
'''


def pytest_html_results_table_header(cells):
    # 添加Description列
    cells.insert(2, html.th("Description"))
    # 添加Time列
    cells.insert(1, html.th("Time", class_="sortable time", col="time"))
    # 删除links列
    cells.pop()


def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.insert(1, html.td(datetime.utcnow(), class_="col-time"))
    cells.pop()


'''
@pytest.hookimpl(hookwrapper=True) 等价于 @pytest.mark.hookwrapper 等价于上面的装饰器
作用：
a：可以获取测试用例不同阶段的结果（setup，call，teardown）
b：可以获取狗子函数的调用结果（yield，返回一个result对象），和调用
结果的测试报告对象（返回一个report对象）
'''
'''
钩子函数的执行顺序：
a：拥有装饰器@pytest.hookimpl(hookwrapper=True)的pytest_runtest_makereport钩子
函数最先被调用运行到yield处
b：pytest_html_results_table_header钩子函数被调用
c：pytest_html_results_table_row钩子函数被调用
d：拥有装饰器@pytest.hookimpl(hookwrapper=True)的pytest_runtest_makereport钩子函数
执行yield之后的代码。yield接收一个Result实例，该实例封装了调用没有装饰器的钩子函数的结果。
并且不能修改结果
'''
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    # item.function.__doc__ 每一个函数得注释信息
    report.description = str(item.function.__doc__)
