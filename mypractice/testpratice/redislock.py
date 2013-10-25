#encoding:utf-8
'''
Created on Oct 25, 2013

@author: liuxue
'''
'''
use redis as lock
'''

from functools import wraps
import redis


class RedisPool(object):
    pool = None
    conn = None
    
    @staticmethod
    def get_pool():
        if not RedisPool.pool:
            RedisPool.pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0, socket_timeout=5)
        return RedisPool.pool
        
    @staticmethod
    def get_redis():
        return redis.Redis(connection_pool=RedisPool.get_pool())
        

def get_redis():
    return RedisPool.get_redis()

def period_lock(key, val='1', exp=0):
    conn = get_redis()
    r = conn.setnx(key, val)
    if r:
        if exp:
            conn.setex(key, exp, val)
        #add func todo
    else:
        pass

def period_loc_dec(key, val='1', exp=0):
    def _decorator(func):
        @wraps(func)
        def wrapper(*args, **kwds):
            conn = get_redis()
            r = conn.setnx(key, val)

            if r:
                print 'GET LOCK'
                if exp:
                    print 'SET EXPRIOD'
                    conn.setex(key, val, exp)
                return func(*args, **kwds)
            else:
                print 'GET NOTHING'
            
        return wrapper
    return _decorator
 
if __name__ == '__main__':
    @period_loc_dec('A', exp=10)
    def test_func():
        return 'A'*2 
    print test_func() 