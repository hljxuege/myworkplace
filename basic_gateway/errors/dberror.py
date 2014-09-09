#encoding:utf-8
'''
Created on Oct 24, 2012

@author: liuxue
'''
from errors.baserror import BaseErrorClass
'''
code from 
'''
class DatabaseError(BaseErrorClass):
    '''
    数据库异常
    当数据库操作出现问题时会抛出该异常
    '''
    code = -3000
    desc_message = u'数据库异常'