#encoding:utf-8
'''
Created on May 19, 2013

@author: liuxue
'''
import threading
import urllib

class TestThread(threading.Thread):
    def run(self):
        for i in xrange(100):
            urllib.urlopen('http://127.0.0.1:9090/').read()

class TestAThread(threading.Thread):
    def run(self):
        for i in xrange(100):
            urllib.urlopen('http://127.0.0.1:9090/A').read()
                    
if __name__ == '__main__':
    tds = []
    tdsA = []
    for i in range(500):
        tt = TestThread()
        tds.append(tt)
    for i in range(500):
        tt = TestAThread()
        tdsA.append(tt)
    l_tds = len(tds)
    
    for i in range(l_tds):
        tds[i].start()
        tdsA[i].start()
        
        