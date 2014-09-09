#encoding:utf-8
'''
Created on: 2012-10-12 13:52
@author: liuxue
'''
from errors.baserror import BaseErrorClass

'''
参数校验失败
1.必填参数为空
2.参数值大于max
3.参数值小于min
4.参数长度大于max
5.参数长度小于min
6.未在选项中
'''
class ValidationError(BaseErrorClass):
    """An error while validating data."""
    code = -40
    desc_message = u'校验错误'
    
