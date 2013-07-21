'''
Created on Jul 15, 2013

@author: liuxue
'''
import sys

from twisted.internet import reactor
from twisted.python import log

from txmysql import client

log.startLogging(sys.stdout)

def example():
    conn = client.MySQLConnection('192.168.0.111', 'root', 'root',
            idle_timeout=120, connect_timeout=30)
    # This gets remembered and re-run if the connection needs reconnection
    d = conn.selectDb("test")
    def selectedDb(ignored):
        
        return conn.runOperation("select * from users")
    d.addCallback(selectedDb)
    def doneInsert(ignored):
        return conn.runQuery("insert into groups (name, do, permit) values('liuxue', 'cando', 'done')")
    d.addCallback(doneInsert)
    def gotResult(data):
        print repr(data)
    d.addCallback(gotResult)
    def handleFailure(reason):
        # reason can be a MySQLError with message, errno, sqlstate, query
        print reason
    d.addErrback(handleFailure)
    return d

if __name__ == "__main__":
    reactor.callWhenRunning(example)
    reactor.run()