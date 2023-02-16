'''
    关键字驱动框架的程序主入口
'''
import os

from python_selenium.class09_ui_frame.excel_driver import excel_read
from python_selenium.class09_ui_frame.my_conf import log_conf

if __name__ == '__main__':
    # 生成日志器
    log = log_conf.get_log('./my_conf/log.ini')
    # excel_read.excel_runner(log)

    # case 的list:用于接收所有的测试用力文件
    cases = []
    # 读取指定路径下的所有文件
    for path, dir, files in os.walk('./data/'):
        for file in files:
            # 获取文件后缀名
            file_type = os.path.splitext(file)
            print(file_type)
            if file_type[1] == '.xlsx':
                excel_path = path + file
                cases.append(excel_path)
                print(excel_path)
            else:
                log.info('文件类型错误{}'.format(file))
        for case in cases:
            excel_read.excel_runner(case, log)
