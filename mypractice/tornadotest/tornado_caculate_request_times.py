#encoding:utf-8
'''
Created on Jul 28, 2013

@author: liuxue
'''
import datetime
import redis
import tornado.httpserver
import tornado.web
settings = {'debug' : True, 'gzip':True} #增加autoreload配置



class RedisPool(object):
    pool = None
    conn = None
    
    @staticmethod
    def get_pool():
        if not RedisPool.pool:
            RedisPool.pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=2, socket_timeout=5)
        return RedisPool.pool
        
    @staticmethod
    def get_redis():
        return redis.Redis(connection_pool=RedisPool.get_pool())
        

def get_redis():
    return RedisPool.get_redis()

def get_r(name):
    r = get_redis()
    keys = r.hkeys(name)
    _l = len(keys)
    for k in keys:
        print r.hget(name, k)
        print r.lrange('%s:%s'%(name, k), 0, _l)
    
    #入库　日期，　名称，次数，平均响应时间，　最小时间，　最大时间
    #生成时间日志　　yyyy-mm-dd.log >> name : value [, value1 ...]
    
    #清理缓存
    r.del
        
class CalcuteHandler(tornado.web.RequestHandler):
    def get(self):
        pass

    def on_finish(self):
        print 1000.0 * self.request.request_time()#请求时间不变
        self._log_request_times()
        print 1000.0 * self.request.request_time()#请求时间不变
        
    def _log_request_times(self):
        request_time = 1000.0 * self.request.request_time()#请求时间不变
        _split_uris = self.request.uri.split('/')
        import time
        time.sleep(2)
        name = 'T' + '.'.join(i for i in _split_uris if i)
        now_date = datetime.datetime.now().strftime('%Y-%m-%d')
        r = get_redis()
        print name
        r.hincrby(now_date, name)
        
        r.rpush(':'.join([now_date, name]), '%.2f'%request_time)
                
application = tornado.web.Application([
    (r"/*", CalcuteHandler),
     ], **settings)

def startup(port=9090):
    server = tornado.httpserver.HTTPServer(application)
    server.listen(port)
    tornado.ioloop.IOLoop.instance().start()
    
if __name__ == '__main__':
    get_r('2013-07-28')
    startup()
    