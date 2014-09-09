#-*- encoding: utf-8 -*-
'''
Created on 2013-02-06

@author: Liuxue
'''

from logging import getLogger
import simplejson
import tornado.web
from uuid import uuid1

class BaseRequestHandler(tornado.web.RequestHandler):
    
    '''
    通用的请求基类
    继承自 tornado.web.RequestHandler
    提供get和post两种请求方式
    '''
    
    def prepare(self):
        self.uuid = str(uuid1())
        self.logger = getLogger('baseservice.common')
        self.sysexcept_logger = getLogger('baseservice.sysexcept')
        req_log = '%s - %s' % (self.request.uri, self.parse_request_param())
        self.logger.info(req_log, extra={'trace': self.uuid})
            
    def get(self):
        '''
        响应get请求
        '''
        pass

    def post(self):
        '''
        响应post请求
        '''
        self.get()
    
    def parse_request_param(self):
        args = self.request.arguments
        
        buf = []
        try:
            for k, v in args.items():
                buf.append('%s=%s'%(k, ','.join([s for s in v])))
        except Exception, e:
            self.logger.info('%s' % str(e), extra={'trace': self.uuid})
             
        return ' -- '.join(buf)
     
    def log_response(self, res):
        '''
        记录响应日志
        '''
        self.logger.info(res, extra={'trace': self.uuid}) 
    
    
    def g(self, name, default=''):
        '''
        包裹get_argument
        '''
        res = self.get_argument(name, default)
        if res == '':
            res = default
        
        return res
        
    def __format_trunk(self, trunk):
        if isinstance(trunk, dict):
            ret = []
            for k,v in trunk.items():
                ret.append('%s:%s'%(k,v))
            return ','.join(ret)    
        else:
            return trunk
        
    def write(self, trunk):
        self.log_response(self.__format_trunk(trunk))  
        res = simplejson.dumps(trunk, indent=2)
        tornado.web.RequestHandler.write(self, res)
        self.flush()

    def get_current_user(self):
        return '111'
