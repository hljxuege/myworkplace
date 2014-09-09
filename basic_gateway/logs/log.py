#encoding:utf-8
'''
Created on Oct 15, 2012

@author: liuxue
'''

from errors.logerror import LoggingConfigException
import logging.config

def initial_logging(file_logging_path):
    try:
        logging.config.fileConfig(file_logging_path)
    except Exception, e:
        raise LoggingConfigException(e)

