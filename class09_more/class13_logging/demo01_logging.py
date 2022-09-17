# loggers:日志器
# handler:处理器
# formatter:格式器
import logging

LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(filename='log.log', filemode='w+', format=LOG_FORMAT,
                    level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S',
                    )
logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")

logging.warning("Some one delete the log file.", exc_info=True, stack_info=True, extra={'user': 'Tom', 'ip':'47.98.53.222'})
