#encoding:utf-8
'''
Created on Jul 18, 2013

@author: liuxue
'''
from tornado import httpclient, gen, options
import tornado.httpserver
from tornado.options import define
from tornado.web import asynchronous
import time
import tornado.web
pretend_service_url = 'http://www.baidu.com'
class PretendService(tornado.web.RequestHandler):
    def head(self):
        pass
    
    @asynchronous
    def get(self):
        print self.__class__
        """ Pretend some work is being done by sleeping for 500ms """
        print '--====---'
        ioloop = tornado.ioloop.IOLoop.instance()
#         ioloop.add_timeout(time.time() + 20, self._finish_req)
        ioloop.add_callback(self._finish_req_a)
        print ">>>>>>>>>>>>>>>>>>>>>>>>>>"
    
    def _finish_req(self):
        print 'over'
        self.finish('over')
    
    def _finish_req_a(self):
        time.sleep(10)
        return self._finish_req()
        
class MainHandlerBlocking(tornado.web.RequestHandler):
    def get(self):
        print self.__class__
        req = httpclient.HTTPRequest(pretend_service_url, method='GET')
        # we could use something like requests or urllib here
        client = tornado.httpclient.HTTPClient()
        response = client.fetch(req)
        import time
        time.sleep(20)
        # do something with the response
      
class MainHandlerAsync(tornado.web.RequestHandler):
    @asynchronous
    def get(self):
        print self.__class__
        req = httpclient.HTTPRequest(pretend_service_url, method='GET')
        client = tornado.httpclient.AsyncHTTPClient()
        client.fetch(pretend_service_url, self._finish_req)
        
    def _finish_req(self, s):
        self.finish('over')
     
application = tornado.web.Application([
    (r"/a", MainHandlerAsync),
    (r"/e", PretendService),
    (r"/b", MainHandlerBlocking)
])
 
if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    print '----start-----'
    tornado.ioloop.IOLoop.instance().start()
    print '----stop-----'
