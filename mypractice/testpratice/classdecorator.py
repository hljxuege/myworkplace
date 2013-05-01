#encoding:utf-8
'''
Created on Apr 28, 2013

@author: liuxue
'''
import functools
def cost_time_deractor(method):
    @functools.wraps(method)
    def wrap(self, *args, **kwargs):
        res = method(self, *args, **kwargs)
        print self.A()
        #计算时间差
        return res
    return wrap
class BaseDAO():
    def A(self):
        print 'logindsa'
    @cost_time_deractor
    def AC(self):
        print '========='   
    def __init__(self):
        self.conn = None
        self.cursor = None

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

if __name__ == '__main__':
    with BaseDAO() as bd:
        bd.AC()
        