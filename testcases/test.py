import logging

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s-[%(filename)s-->line:%(lineno)d]-%(levelname)s:%(message)s')

logging.info("aaa")
logging.error("bbb")