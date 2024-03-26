import logging

# 1，创建日志记录器
logger = logging.getLogger('wb')
logger.setLevel('INFO')

# 2，创建日志处理器
filehandle = logging.FileHandler(filename='myfile.log',encoding='utf-8')
filehandle.setLevel('INFO')

# 3，创建格式化器
formatter = logging.Formatter(fmt='%(asctime)s-[%(filename)s-->line:%(lineno)d]-%(levelname)s:%(message)s')
filehandle.setFormatter(formatter)

logger.addHandler(filehandle)


logger.info('this is my first logger')
logger.error('this is my firest error')