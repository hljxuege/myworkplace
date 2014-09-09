#encoding:utf-8
'''
Created on Sep 9, 2014

@author: liuxue
'''
from util.except_util import except_decorator


class BaseService():
    name = 'base'
    
    def __init__(self, req):
        self.req = req
        
    @except_decorator
    def process(self, **kwargs):
        return self.name