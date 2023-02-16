'''
    生成日志器得配置
'''
import logging.config


# 路径一定要在调用得地方填写，不然会报错
def get_log(path):
    logging.config.fileConfig(path, encoding='utf-8')
    return logging.getLogger()
