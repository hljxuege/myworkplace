#encoding:utf-8
'''
Created on 2012-7-4

@author: Liuxue
'''
from configs.config import PROJECT_CODE
from errors.baserror import BaseErrorClass, BaseEEClass

def except_decorator(func):
    def wrapper(self, *args,**dic):
        try:
            e = None
            data = None
            data = func(self, *args,**dic)
        except Exception, e:
            pass
        finally:
            ret = 0
            message = 'success'
            #返回信息
            if e:
                if not isinstance(e, BaseEEClass):
                    e = BaseErrorClass(e)
                ret = e.code - (PROJECT_CODE)
                message = e.info_message
                
                logging_message = e.exception_message
                self.sysexcept_logger.exception(e)
                self.logger.error(logging_message)
                self.logger.exception(e)
                
            val = {}    
            val['return_code'] = ret
            val['return_message'] = message
            if data != None:
                val['data'] = data
            return val
        
    return wrapper

def handler_except_deractor(method):
    def wrap(self, *args, **kwargs):
        try:
            e = None
            method(self, *args,**kwargs)
            ret = 0
            message = 'success'
        except Exception, e:
            pass
        finally:
            if e:
                if not isinstance(e, BaseEEClass):
                    e = BaseErrorClass(e)
                ret = e.code - (PROJECT_CODE)
                message = e.info_message
                
                logging_message = e.desc_message+e.exception_message
                self.sysexcept_logger.error(logging_message)
                self.logger.error(logging_message)
                self.logger.exception(e)
                
            val = {}    
            val['return_code'] = ret
            val['return_message'] = message
            
            if ret < 0:#成功返回，不能输出任何数据
                self.write(val)
            return val
                        
    return wrap