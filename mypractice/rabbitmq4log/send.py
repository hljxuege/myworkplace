#encoding:utf-8
'''
Created on Dec 28, 2013

@author: liuxue
'''
import pika
import simplejson


connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logcenter',
                         type='direct')

severity = 'warning'
message = 'Hello World!'
m = {
'host_name':'cbs_web',
'trace_code':'uuid',
'project_code':'',
'title':'',
'log_datetime':'2013-12-12 12:21:09',
'message':'日志信息'
}
message = simplejson.dumps(m)
channel.basic_publish(exchange='logcenter',
                      routing_key=severity,
                      body=message)
print " [x] Sent %r:%r" % (severity, message)
connection.close()