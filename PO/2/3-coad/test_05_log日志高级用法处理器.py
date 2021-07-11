#1.导包
import logging.handlers

#创建日志器
logger = logging.getLogger()
#设置打印的日志级别
logger.setLevel(level=logging.INFO)


#创建输出到控制台的处理器对象
ls = logging.StreamHandler()

#创建每日生成一个日志文件时，要导包logging里的handlers的方法
lht = logging.handlers.TimedRotatingFileHandler()

#通过日志器打印日志到指定位置，需要添加处理器
logger.addHandler()





#3.打印日志
logger.info("高级用法的打印日志")