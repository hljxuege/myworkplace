#encoding:utf-8
'''
Created on Oct 24, 2012

@author: liuxue
'''
#from config.consist import STATUS_CODE
class BaseEEClass(Exception):
    '''
    api中ExcepitonClass与ErrorClass的父类
    '''
    code = -1
    desc_message = 'Base Error or exception'
    default_message = ''
    exception_message = ''
    def __init__(self, message='', error_desc=''):
        self.exception_message = ':'.join([ i for i in [self.default_message, str(message), str(error_desc)] if i])
        self.info_message = ':'.join([i for i in [self.desc_message, str(message)] if i])
        
    def __call__(self):
        print self
    
    def __str__(self):
        return '%s:%s'%(self.desc_message, self.exception_message)
    
class BaseExceptionClass(BaseEEClass):
    '''
    基础异常类
    '''
    code = -2
    desc_message = u'系统异常'

class BaseErrorClass(BaseEEClass):
    '''
    基础错误类
    '''
    desc_message = u'系统错误'    