import os

import pytest


def init_env():
    '''
    初始化图片目录
    '''
    os.mkdir('./test_report' + '/image')


def run():
    # init_env()
    pytest.main(['-s', '-v',
                 # 报告存放路径
                 '--html=./test_report/report.html',
                 # 捕获错误日志输出信息到测试报告
                 '--capture=sys',
                 # 把css样式合并到html里,避免分享时css样式丢失
                 '--self-contained-html',
                 # 设置最大失败次数
                 '--maxfail', '5',
                 # 设置失败重跑次数
                 '--reruns', '1'])


if __name__ == '__main__':
    run()
