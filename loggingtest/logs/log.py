#encoding:utf-8
'''
Created on Dec 31, 2013

@author: liuxue
'''
import logging.config

def get_logger(name=''):
    try:
        logging.config.fileConfig('logging.conf')
    except Exception, e:
        raise e

    try:
        logger = logging.getLogger(name)
    except Exception, e:
        raise e
    return logger

if __name__ == '__main__':
    print get_logger().info('')