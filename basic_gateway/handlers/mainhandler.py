#encoding:utf-8
'''
Created on 2012-5-18

@author: Liuxue
'''
from logging import getLogger

import tornado.httpserver
import tornado.ioloop
import tornado.web

from handlers.basehandler import BaseRequestHandler


logger = getLogger('baseservice.common')
DEBUG = False
settings = {'debug':DEBUG} #增加autoreload配置

class BaseService():
    name = 'base'
    
    def process(self, **kwargs):
        return self.name

class ProcessService(BaseService):
    name = 'process'
    
app = {
       'base': BaseService,
       'process': ProcessService,
       }

class GatewayHandler(BaseRequestHandler):
    def get(self):
        method = self.g('method', 'base')
        
        
        service = app[method]()
        
        self.write(service.process())
        

apps = [(r"/gateway", GatewayHandler),
        ]
    
application = tornado.web.Application(apps, **settings)


def startup(port=9090):
    server = tornado.httpserver.HTTPServer(application)
    server.listen(port)
    logger.info('tornado start')
    tornado.ioloop.IOLoop.instance().start()
