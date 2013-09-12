#encoding:utf-8
'''
Created on Aug 30, 2013

@author: liuxue
'''
from MySQLdb.connections import Connection
from MySQLdb.cursors import DictCursor
from functools import partial
from tornado import gen, ioloop
from tornado.web import RequestHandler, asynchronous
import tornado.httpserver
'''
use tornado-mysql, tornado-redis and mongotor 
'''
class EPollConnection(Connection):
    """.
        non-blocking mysql connection for read
        for tornado ioloop
    """
    def epoll_query(self, query, callback=None, on_error=None, args=None):
        """ Non-blocking query. callback is function that takes list
            of tuple args """
        self.send_query(query)
        ioloop.IOLoop.instance().add_handler(self.fd,
            partial(self._handle_read, callback=callback, on_error=on_error), ioloop.IOLoop.READ)

    def _handle_read(self, fd, ev, callback=None,on_error=None):
        res = []
        try:
            self.read_query_result()
            result = self.use_result()
            while True:
                row = result.fetch_row()
                if not row:
                    break
                res.append(row[0])
            callback(res)
        except Exception, e:
            if on_error:
                return on_error(e)
            else:
                raise e
        finally:
            self._cleanup()

    def _cleanup(self):
            ioloop.IOLoop.instance().remove_handler(self.fd)

def get_conn():
    return EPollConnection(host="192.168.0.111",user="babby",passwd="love",db="babbylove",charset="utf8", cursorclass=DictCursor)      
class BaseHandler(RequestHandler):
    def initialize(self):
        self.db = None
        self.return_value = None
    def prepare(self):
        '''
        记录请求日志
        '''
        print self.parse_request_param()
    
    def finish(self, chunk=None):
        '''
        重写服务的finish,　并存储返回值
        '''
        
        RequestHandler.finish(self, chunk=chunk)
        self.return_value = chunk
        
    def on_finish(self):
        '''
        清理数据库链接，并记录返回的数据
        '''
        if self.db:
            self.db.close()
            
    def parse_request_param(self):
        args = self.request.arguments
        buf = []
        try:
            for k, v in args.items():
                buf.append('%s=%s'%(k, ','.join([s for s in v])))
        except Exception, e:
            pass
             
        return ' -- '.join(buf)
class GetUsersHander(BaseHandler):
    '''
    获取所有用户
    '''
    @asynchronous
    @gen.engine
    def get(self):
        self.db = get_conn()
        r = yield gen.Task(self.db.epoll_query, "select name, passwd from user")
        print r
        self.finish('')


apps = []
apps.extend([
             (r"/get", GetUsersHander),
             ])
    
application = tornado.web.Application(apps, **{})

def startup(port=9090):
    server = tornado.httpserver.HTTPServer(application)
    server.listen(port)
    tornado.ioloop.IOLoop.instance().start()  

if __name__ == '__main__':
    startup()        
