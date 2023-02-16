'''
    测试套件:
        就相当于是一个list,说白了就是一个文件夹
        在默认的UnitTest框架下,所有的用例都是会全部执行,且执行时是依照UnitTest自定义的排序规则
        如果说需要调用部分的测试用例,来执行冒烟测试,就无法在默认的UnitTest下实现
        所以可以基于套件的形态将需要调用的测试用例提取出来进行执行,从而自动化实现测试效果
        还可以基于jenkins持续集成时,一键运行指定测试用例
        甚至于在用例并发运行是,也可以隐形通过调用套件来实现并行处理
'''
import unittest


from python_selenium.class11_suite_runner.unit_demo import UnitDemo
# 创建套件
# suite = unittest.TestSuite()
# # 添加测试用例
# suite.addTest(UnitDemo('test_05'))
# suite.addTest(UnitDemo('test_02'))
# suite.addTest(UnitDemo('test_03'))
# # 创建运行器
# runner = unittest.TextTestRunner()
# # 基于运行器来执行套件
# runner.run(suite)

# 添加多个用例到套件:可以基于list来实现
# suite = unittest.TestSuite()
# cases = [UnitDemo('test_05'), UnitDemo('test_02'), UnitDemo('test_03')]
# suite.addTests(cases)
# runner = unittest.TextTestRunner()
# runner.run(suite)

# 添加多个用例到套件:通过添加一整个UnitTest类作为套件中的用例
# suite = unittest.TestSuite()
# suite.addTests(unittest.TestLoader().loadTestsFromTestCase(UnitDemo))
# # 添加多个用例到套件:通过Name来实现,文件名.class名
# # suite.addTests(unittest.TestLoader().loadTestsFromName('unit_demo.UnitDemo'))
# runner = unittest.TextTestRunner()
# runner.run(suite)

# 添加路径下所有测试用例,组成套件
# 定义用例的路径
case_dir = './'
# discover就是一个套件
discover = unittest.defaultTestLoader.discover(start_dir=case_dir, pattern='u*.py')
runner = unittest.TextTestRunner()
runner.run(discover)

# 运行器,verbosity是日志等级0-1-2
# runner = unittest.TextTestRunner(verbosity=2)
# runner.run(discover)

# HTMLTestRunner 导入后，生成新的html报告格式
