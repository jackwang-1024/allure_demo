import logging
import os.path

def getlogger():

    # 1，创建日志记录器
    logger = logging.getLogger('wb')
    logger.setLevel('INFO')

    # 2，创建日志处理器
    # project_path = os.path.dirname(os.getcwd())
    # # C:\learning\python\code
    # log_path = project_path + "\\outputs\\logs\\myfile.log"

    filehandle = logging.FileHandler(filename='C:\\learning\\python\\code\\outputs\\logs\\myfile.log', encoding='utf-8')
    filehandle.setLevel('INFO')

    # 3，创建格式化器
    formatter = logging.Formatter(fmt='%(asctime)s-[%(filename)s-->line:%(lineno)d]-%(levelname)s:%(message)s')
    filehandle.setFormatter(formatter)

    logger.addHandler(filehandle)

    return logger
