'''
POM
    关键字驱动设计模式,是所有测试框架的核心底层
    目前市场主流的测试框架设计模式分为两种:
        1.关键字驱动,一般用于接口自动化测试,和部分UI自动化,一般是izai多个系统要
        执行自动化测试时,应用这种模式.在不同系统中,都要写很多重复性的代码.
        2.POM,页面对象模型,用于专门针对一个系统执行自动化测试实现的设计模式.
        可以最大程度实现测试的覆盖率.也是目前行业内工人最佳的设计模式
        POM,Page Object Module,页面对象模型，PO是专门以页面作为自动化测试的
        执行对象，来事项整体自动化测试的。
        POM：
            进入登录页，执行登录操作
            进入商品详情页，执行添加商品到购物车操作
            进入购物车页面，执行校验添加是否成功操作
            完全基于业务流程，以及页面来实现的自动化测试
            系统所有的页面，都是基于url来进行定位的，每一个页面都有一个对应的url
            基于页面来实现页面中的流程
            POM中，基于系统定义不同的页面对象，来实现不同页面的一个或者多个流程。再基于
            多个页面对象得拼接，实现一个完整得系统业务流程，相较于关键字驱动而言，会更加
            适用于系统本身流程测试
        POM实现：
            1.工程结构 ：
                代码与数据进行分离，逻辑代码与测试代码得分离
                基类：关键字驱动类得POM设计形变
                页面对象类：提取系统中关键得页面，封装成页面对象，便于测试执行
                    页面类：封装页面得操作行为
                    页面数据类：封装页面得元素及属性
                测试用例类：测试代码得实现
                测试数据类：管理测试数据
            2.源码
            3.POM的覆盖率高还是低取决于你的页面对象的设计
            4.自动化测试是否能够执行取决于你的手艺和产出成本比

'''
'''
    基类：pom体系下得底层代码，用于封装各类行为操作，便于页面对象类进行调用。
        根本核心是关键字驱动设计理念
'''
import time

from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def visit(self, text):
        self.driver.get(text)

    def quit(self):
        self.driver.quit()

    def locator(self, loc):
        return self.driver.find_element(*loc)

    def input(self, loc, text):
        self.locator(loc).send_keys(text)

    def click(self, loc):
        self.locator(loc).click()

    def sleep(self, text):
        time.sleep(int(text))

    def wait(self, loc):
        WebDriverWait(self.driver, 10, 0.5).until(lambda e1: self.locator(*loc), '等待失败')

    def assert_text(self, loc, text):
        try:
            assert text == self.locator(loc).text, '断言失败'
            return True
        except:
            return False
