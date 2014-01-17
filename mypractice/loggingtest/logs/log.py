#encoding:utf-8
'''
Created on Dec 31, 2013

@author: liuxue
'''
from configs.config import LOG_CONFIG_FILE
from errors.logerror import LoggingConfigException, GetLoggingException
import logging.config

def get_logger(name=''):
    try:
        logging.config.fileConfig(LOG_CONFIG_FILE)
    except Exception, e:
        raise LoggingConfigException(e)

    try:
        logger = logging.getLogger(name)
    except Exception, e:
        raise GetLoggingException(e)
    return logger

if __name__ == '__main__':
    print get_logger().info('')