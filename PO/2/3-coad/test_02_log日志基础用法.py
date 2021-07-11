#1.导包
import logging

#2.设置日志级别
logging.basicConfig(level=logging.DEBUG)  #logging中默认的日志级别为WARNING，程序中大于等于该级别的日志才能输出，小于该级别的日志不会被打印出 来

#3.打印日志

logging.debug("调试级别，打印非常详细的日志信息，通常用于对代码的调试")
logging.info("信息级别，打印一般的日志信息，突出强调程序的运行过程")
logging.error("错误级别，打印错误异常信息，该级别的错误可能会导致系统的一些功能无法正常使用")
logging.warning("警告级别，打印警告日志信息，表明会出现潜在错误的情形，一般不影响软件的正常使用")
logging.critical("严重错误级别，一个严重的错误，这表明系统可能无法继续运行")
