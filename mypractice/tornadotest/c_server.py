#encoding:utf-8
'''
Created on May 19, 2013

@author: liuxue
'''
import threading
import urllib
class TestThread(threading.Thread):
    def run(self):
        for i in xrange(1000):
            urllib.urlopen('http://127.0.0.1:9090/').read()
        
if __name__ == '__main__':
    tds = []
    for i in range(1000):
        tt = TestThread()
        tds.append(tt)
    for t in tds:
        t.start()