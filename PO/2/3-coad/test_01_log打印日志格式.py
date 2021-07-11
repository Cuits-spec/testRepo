# 1.导包
import logging

# 2.设置日志格式

logging.basicConfig(format="%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")

# 3.打印日志

logging.debug("调试级别")
logging.info("信息级别")
logging.error("错误级别")
logging.warning("警告级别")
logging.critical("严重错误级别")
