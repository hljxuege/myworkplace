#encoding:utf-8
'''
Created on Oct 15, 2012

@author: liuxue
'''
import logging
from logging.handlers import TimedRotatingFileHandler
import time


#实现一个文件日志处理类
class IHTimedRotatingFileHandler(TimedRotatingFileHandler):
    def shouldRollover(self, record):
        now = time.time()
        t = int(now)
        if t >= self.rolloverAt:
            return 1
        elif (now/self.interval) > (self.rolloverAt/self.interval):
            return 1
        #print "No need to rollover: %d, %d" % (t, self.rolloverAt)
        return 0

class IHFormatter(logging.Formatter):

    def format(self, record):
        if not hasattr(record, 'trace'):
            record.trace = '-'
        return super(IHFormatter, self).format(record)
        