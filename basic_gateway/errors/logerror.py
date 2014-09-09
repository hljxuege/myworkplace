#encoding:utf-8
'''
Created on Oct 24, 2012

@author: liuxue
'''
from errors.baserror import BaseExceptionClass
'''
#code from 30~60
'''
class LoggingConfigException(BaseExceptionClass):
    '''
    api日志配置错误：获取日志配置错误
    '''
    code = -31
    desc_message = u'获取日志配置错误'
    
class GetLoggingException(BaseExceptionClass):
    '''
    api日志配置错误：未找到该日志处理
    '''
    code = -32
    desc_message = u'未找到该日志处理'