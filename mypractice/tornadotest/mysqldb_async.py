'''
Created on Aug 30, 2013

@author: liuxue
'''
from functools import partial
from tornado import ioloop
from MySQLdb import *
from MySQLdb.connections import Connection
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
            
