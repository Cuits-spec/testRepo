# 1.导包
import logging.handlers

# 创建日志器
logger = logging.getLogger()
# 设置打印的日志级别
logger.setLevel(level=logging.INFO)

# 创建输出到控制台的处理器对象
ls = logging.StreamHandler()

# 创建每日生成一个日志文件时，要导包logging里的handlers的方法,
# filename意思文件路径，when时间单位M意思分钟，interval每隔一分钟创建一个，backupCount创建2个的时候就删除第一个
lht = logging.handlers.TimedRotatingFileHandler(filename="./log//text.log", when="M", interval=1, backupCount=2)

# 创建格式化器
formatter = logging.Formatter(
    fmt="%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")

# 给处理器设置格式化器
ls.setFormatter(formatter)
lht.setFormatter(formatter)
