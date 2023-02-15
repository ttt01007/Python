import os.path

import pytest
from selenium import webdriver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            # extra.append(pytest_html.extras.html("<div>Additional HTML</div>"))
            # 将测试用例的nodeid作为截图文件的名字
            # 处理::符号,替换为_
            case_path = report.nodeid.replace('::', '_') + '.png'
            # 定义方法,实现本地截图
            capture_screenshots(case_path)
            # 需要处理case_path,不能用/. 以/为分隔符,保留最后一段
            image_path = 'image/' + case_path.split('/')[-1]
            if image_path:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align= "right"/></div>' % image_path
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def capture_screenshots(case_path):
    '''
        配置用例失败截图路径,以用例nodeid保存图片
    '''
    global driver
    # 需要处理case_path,不能用/. 以/为分隔符,保留最后一段
    file_name = case_path.split('/')[-1]
    # 生命图片的保存路径
    image_dir = os.path.join('test_report', 'image', file_name)
    # 浏览器驱动,在用例前置里实例化
    driver.save_screenshot(image_dir)


@pytest.fixture(scope='session', autouse=True)
def browser():
    '''全局定义浏览器启动'''
    global driver
    driver = webdriver.Edge()
    return driver


# 关闭浏览器
@pytest.fixture(scope='session', autouse=True)
def browser_close():
    yield driver
    driver.quit()
    print("test end!")
