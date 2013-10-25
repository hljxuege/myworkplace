#encoding:utf-8
'''
Created on Oct 25, 2013

@author: liuxue
'''
from functools import wraps

OPNE_REDIS = True
basic_type = (int, str, bool, unicode)
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
def pre_args_decorator(is_open=OPNE_REDIS, key='TEST', safemode=False, expire=0):
    '''
    if type(ret) is not str, you should use safemode=True
    '''
    def _query_redis_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if is_open:
                if args:
                    name = '%s:%s' %(key, ':'.join(map(lambda x:str(x),filter(lambda x : isinstance(x, basic_type), args))))
                else:
                    name = key
                redis_conn = get_redis()
                ret = redis_conn.get(name)
                if ret:
                    if safemode:
                        ret = eval(ret)
                else:
                    ret = func(*args)
                    if ret :#如果有内容，则缓存
                        if expire > 0:
                            redis_conn.setex(name, ret, expire)
                        else:
                            redis_conn.set(name, ret)
            else:    
                ret = func(*args, **kwargs)
            return ret
        return wrapper
    return _query_redis_decorator

def post_args_decorator(is_open=OPNE_REDIS, key='TEST', expire=0):
    def _decorator(func):
        @wraps(func)
        def wrapper(*args, **kwds):
            if is_open:
                if args:
                    name = '%s:%s' %(key, ':'.join(map(lambda x:str(x),filter(lambda x : isinstance(x, basic_type), args))))
                else:
                    name = key
                redis_conn = get_redis()
                ret = func(*args)
                if ret :#如果有内容，则缓存
                    if expire > 0:
                        redis_conn.setex(name, ret, expire)
                    else:
                        redis_conn.set(name, ret)
            else:
                pass
        return wrapper
    return _decorator