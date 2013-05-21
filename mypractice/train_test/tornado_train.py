#encoding:utf-8
'''
Created on May 21, 2013

@author: liuxue
'''
from train_test.query_train import query_train
from train_test.ticket_query import ticket_query
import simplejson
import tornado.httpserver
import tornado.web
class BasseHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Welcome to come with Liuxue')
    
    def post(self):
        self.get()
    
    def write(self, trunk):
        res = simplejson.dumps(trunk)
        tornado.web.RequestHandler.write(self, res)
        
class QueryTrainHandler(BasseHandler):
    def get(self):
        from_station, to_station, date = self.get_argument('from_station'), self.get_argument('to_station'), self.get_argument('date')
        data = ticket_query(str(from_station), str(to_station), str(date))
        print data
        for i in data:
            for j in  i.values():
                print j
        self.write({'data':data, 'num':len(data)})
    
class QueryTicketHandler(BasseHandler):
    def get(self):
        from_station, to_station, date = self.get_argument('from_station'), self.get_argument('to_station'), self.get_argument('date')
        data = query_train(str(from_station), str(to_station), str(date))
        self.write({'data':data, 'num':len(data)})
    
settings = {'debug' : True}
application = tornado.web.Application([
    (r"/", BasseHandler),
    (r"/queryTrain", QueryTrainHandler),
    (r"/queryTicket", QueryTicketHandler),
     ], **settings)

def startup(port=9999):
    server = tornado.httpserver.HTTPServer(application)
    server.listen(port)
    print 'start' 
    tornado.ioloop.IOLoop.instance().start()
    print 'stop' 
    
if __name__ == '__main__':
    startup()