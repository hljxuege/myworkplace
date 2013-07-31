#encoding:utf-8
'''
Created on Jul 30, 2013

@author: liuxue
'''
FLUSH_REIDS_TIME = 10
from threading import Timer
class TimerService(object):
    def __init__(self, callback, callback_time=1800):
        self.callback = callback
        self.callback_time = callback_time
        self._running = False

    def start(self):
        """Starts the timer."""
        self._running = True
        self._schedule_next()

    def stop(self):
        self._running = False

    def _run(self):
        if not self._running:
            return
        try:
            self.callback()
        except Exception, e:
            raise e
        self._schedule_next()

    def _schedule_next(self):
        if self._running:
            self.timer = Timer(self.callback_time,self._run)
            self.timer.start() 

class PeriodUpdateFlightTimerService(TimerService):
    def __init__(self, callback, callback_time=FLUSH_REIDS_TIME):
        super(PeriodUpdateFlightTimerService, self).__init__(callback, callback_time)
        
    def _run(self):
        if not self._running:
            return
        try:
            self.callback()
        except Exception, e:
            raise e
        self._schedule_next()

def _get_expire_time():
    expire_time = 10
    return expire_time + expire_time/2 #时间
                
