'''
Created on Jul 16, 2013

@author: liuxue
'''
from MySQLdb.connections import Connection
from MySQLdb.cursors import DictCursor
from functools import partial
from tornado import gen, ioloop
import json
import logging
import tornado.httpserver
import tornado.web

class EPollConnection(Connection):
    """.
        non-blocking mysql connection
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


class MainHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        conn=EPollConnection(host="192.168.0.111",user="babby",passwd="love",db="babbylove",charset="utf8", connect_timeout=5)
        conn.epoll_query("select * from user",callback=self.do_res)

    def do_res(self,res):
        self.finish('xxx'+json.dumps(res))
        
    def log_request(self, handler):
        log_method = logging.info
        request_time = 1000.0 * handler.request.request_time()
        log_method("%d %s %.2fms", handler.get_status(),
                   handler._request_summary(), request_time)
        
        
        self.log_request(handler)

def do_res(res):
    return res           
def get_conn(*args):
    return EPollConnection(host="192.168.0.111",user="babby",passwd="love",db="babbylove",charset="utf8", cursorclass=DictCursor, connect_timeout=5)
        
class MysqlAsyncHandler(tornado.web.RequestHandler):
        
    @tornado.web.asynchronous
    @gen.engine
    def get(self):
        a = int(self.get_argument('a', 20))
        
        print a
        self.conn = get_conn()
        r = yield gen.Task(self.conn.epoll_query, "select sleep(%s)"%a)
        print '%s f'%a
        self.finish()
    
    def on_finish(self):
        if self.conn:
            self.conn.close()
         
application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/m1", MysqlAsyncHandler),
     ], **{})

def startup(port=9090):
    server = tornado.httpserver.HTTPServer(application)
    server.listen(port)
    tornado.ioloop.IOLoop.instance().start()
    
if __name__ == '__main__':
    startup()
    