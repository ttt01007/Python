# 套件
import unittest

from class11_suite_runner.unit_demo import UnitDemo

# 创建套件
suite = unittest.TestSuite()
# 添加测试用例
# suite.addTest(UnitDemo('test_05'))
# suite.addTest(UnitDemo('test_02'))
# suite.addTest(UnitDemo('test_03'))

# 添加class中全部测试用例
# suite.addTests(unittest.TestLoader().loadTestsFromTestCase(UnitDemo))
# suite.addTests(unittest.TestLoader().loadTestsFromName('unit_demo.UnitDemo'))

# 添加路径下所有测试用例,组成套件
case_dir = './'
discover = unittest.defaultTestLoader.discover(start_dir=case_dir, pattern='u*.py')

# 运行器,verbosity是日志等级0-1-2
runner = unittest.TextTestRunner(verbosity=2)
runner.run(discover)

# HTMLTestRunner 导入后，生成新的html报告格式