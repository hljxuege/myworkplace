#encoding:utf-8
'''
Created on Sep 9, 2014

@author: liuxue
'''
#encoding:utf-8
'''
Created on 2012-5-18

@author: Liuxue
'''

from logging import getLogger

import tornado.httpserver
import tornado.ioloop
import tornado.web

from configs.config import DEFAULT_PORT, DEFAULT_APP_CONFIG_PATH, \
    DEFAULT_LOG_CONFIG_PATH
from handlers.basehandler import BaseRequestHandler
from services.baseservice import BaseService
from services.otherservice import ProcessService
from logs.log import initial_logging
from util.dbutil import initial_mysql
from util.parseconfig import initial_sys_config, get_sys_config
from util.redisutil import initial_redis

logger = getLogger('baseservice.common')
DEBUG = False
settings = {'debug':DEBUG} #增加autoreload配置
    
app = {
       'base': BaseService,
       'process': ProcessService,
       }

class GatewayHandler(BaseRequestHandler):
    def get(self):
        method = self.g('method', 'base')
        
        service = app[method](self)
        
        self.write(service.process())
        

apps = [(r"/base/gateway", GatewayHandler),
        ]
    
application = tornado.web.Application(apps, **settings)

def initial_all(args):
    #initial_logging
    initial_logging(args.logging_config_path)
    #initial_sys_config
    initial_sys_config(args.configure)
    #initial_redis
    redis = get_sys_config('REDIS')
    initial_redis(redis['host'], redis['port'], redis['name'], redis['timeout'])
    getLogger('baseservice.common').info('REDIS STATUS OK')
    
    #initial_mysql
    mysql = get_sys_config('MYSQL')
    initial_mysql(mysql['host'], mysql['port'], mysql['name'], mysql['user'], mysql['pswd'], mysql['timeout'])
    getLogger('baseservice.common').info('MYSQL STATUS OK')
    
def check_app():
    for k, s in app.items():
        service = s(None)
        assert k == service.name, '%s diff %s'%(k, service.__class__.__name__)

def startup(port=9090):
    server = tornado.httpserver.HTTPServer(application)
    server.listen(port)
    logger.info('tornado start')
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    import argparse
    default_port = DEFAULT_PORT
    default_app_config_path = DEFAULT_APP_CONFIG_PATH
    default_log_config_path = DEFAULT_LOG_CONFIG_PATH
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default = default_port, \
                        help="server listenning port, default is %d"%default_port)
    parser.add_argument("--configure", default = default_app_config_path,
                        help="app need configure file path, and the default value : %s"%default_app_config_path)
     
    parser.add_argument("--logging_config_path", default = default_log_config_path,
                        help="global logging configure file, and the default value :%s"%default_log_config_path)
     
    parser.add_argument("--flush_redis", action="store_true",
                        help="use this to flush redis, example: python baseservice --flush_redis, and then the redis flushed")
    
    args = parser.parse_args()
    #初始化
    initial_all(args)
    getLogger('baseservice.common').info('INITIAL COMPLETED')
    
    check_app()
    # start the http service
    startup(args.port)