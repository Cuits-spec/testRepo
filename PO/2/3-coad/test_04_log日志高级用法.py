#1.导包
import logging

#创建日志器
logger = logging.getLogger()
#设置打印的日志级别
logger.setLevel(level=logging.INFO)
#通过日志器打印日志到指定位置，需要添加处理器
logger.addHandler()





#3.打印日志
logger.info("高级用法的打印日志")