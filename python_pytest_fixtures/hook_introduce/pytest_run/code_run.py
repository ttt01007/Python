from _pytest import runner

# runner源码中方法：pytest_runtest_makereport
# 这里item是测试用例，call是调用过程
# 先执行when=‘setup’，返回setup的结果
# 先执行when=‘call’，返回call的结果
# 先执行when=‘teardown’，返回teardown的结果
