#encoding:utf-8
'''
Created on Dec 31, 2013

@author: liuxue
'''
from configs.config import LOG_PATH
from logging import FileHandler
import datetime
import os
#实现一个文件日志处理类
class FileLogHandler(FileHandler):
    def __init__(self, pre='', *args, **kwargs):
        filename = '%s%s' %(pre, datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d.log'))
        log_file = os.path.join(LOG_PATH, filename)
        super(FileLogHandler, self).__init__(log_file, *args, **kwargs)

        