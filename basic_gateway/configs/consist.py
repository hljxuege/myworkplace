#encoding:utf-8
'''
Created on Oct 13, 2012

@author: liuxue
'''

STATUS_CODE = {
    #成功
    '0' : {'return_code' :0, 'return_message': 'success'},
    
    #失败
    '-1' : {'return_code' :-1, 'return_message': u'对不起，系统繁忙，请您稍后再试'},
    
    #异常
    '-2' : {'return_code' :-2, 'return_message': u'对不起，系统繁忙，请您稍后再试'},
    
    #api
    #10~999
    #api.log
    #30~40
    '-31' : {'return_code' :-31, 'return_message': u'获取日志配置错误'},#LoggingConfigException
    '-32' : {'return_code' :-32, 'return_message': u'未找到该日志处理'},#GetLoggingException
    '-33' : {'return_code' :-33, 'return_message': u'无法从session中获取usercode'},#SessionInvalidateError
    #api.form
    #40~45
    '-40': {'return_code' :-40, 'return_message': u'校验错误'},#ValidationError
    #1000~1999
    
    #db
    '-3000':{'return_code' :-3000, 'return_message': u'数据库异常'},#DatabaseError
    #service
    #3001~3500
    #invoice
    '-3001':{'return_code' :-3001, 'return_message': u'发票数据未找到'},#InvoiceRecordNotFoundError
    '-3002':{'return_code' :-3002, 'return_message': u'发票数据不存在'},#InvoiceRecordNotExistException
    
    #shipping
    '-3101':{'return_code' :-3101, 'return_message': u'物流记录中，is_defalut字段违背唯一性约束'},#ShippingDefaultRecordError
    '-3102':{'return_code' :-3102, 'return_message': u'物流记录不存在'},#ShippingRecordNotExistException
    '-3103':{'return_code' :-3103, 'return_message': u'物流记录未找到'},#ShippingRecordNotFoundError
    
    #cal
    '-3201':{'return_code' :-3201, 'return_message': u'未找到相应的理财信息'},#RateRecordNotFoundException
    #push
    '-3401':{'return_code' :-3401, 'return_message': u'未找到相应的PUSH配置信息'},#PushConfigNOTFOUNDError
    #handler
    #8000
    }