#-*- encoding: utf-8 -*-
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
    
if __name__ == "__main__":

    c = get_redis()
    c.set('foo', 'HELLO')
    keys = c.keys('*')
    print keys
    c.delete(*keys)
    print c.get('foo')