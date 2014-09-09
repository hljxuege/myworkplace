#-*- encoding: utf-8 -*-
import redis

class RedisPool(object):
    pool = None
    conn = None
    @staticmethod
    def load(host, port, db, timeout):
        RedisPool.pool = redis.ConnectionPool(host=host, port=port, \
                                              db=db, socket_timeout=timeout)
        
        assert redis.Redis(connection_pool=RedisPool.pool).ping(), "REDIS STATUS BAD"
        
    @staticmethod
    def get_redis():
        return redis.Redis(connection_pool=RedisPool.pool)

def initial_redis(host, port, db, timeout):     
    RedisPool.load(host, port, db, timeout)

def get_redis():
    return RedisPool.get_redis()

