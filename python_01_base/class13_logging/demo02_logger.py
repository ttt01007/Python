import datetime
import logging
import logging.handlers

logger1 = logging.getLogger('logger1')
logger1.setLevel(logging.DEBUG)

# 根据时间，每天0点进行切割日志
rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7,
                                                       atTime=datetime.time(0, 0, 0, 0))
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

f_handler = logging.FileHandler('error.log')
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

s_handler = logging.StreamHandler()
s_handler.setLevel(logging.ERROR)
s_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))


logger1.addHandler(rf_handler)
logger1.addHandler(f_handler)
logger1.addHandler(s_handler)

logger1.debug('debug message')
logger1.info('info message')
logger1.warning('warning message')
logger1.error('error message')
logger1.critical('critical message')