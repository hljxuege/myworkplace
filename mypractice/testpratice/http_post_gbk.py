#encoding:utf-8
'''
@description:
模拟爱特博退票回调操作。
'''
import os
import urllib, urllib2 
file_abs_path = os.path.abspath(__file__)
rename_path = os.path.dirname(__file__)

url = 'http://127.0.0.1'

def change_to_gb2312(s):
    return s.decode('utf-8').encode('gb2312')

def chang_param_to_gb2312(p):
    r = {}
    for k,v in p.items():
        r.update({change_to_gb2312(k):change_to_gb2312(v)})
        
    return r

if __name__ == '__main__':
#     if __file__ != 'fake_callback.py':
#         raise 'Bad File name'
    _p = {
        'data' : u'',
        'MsgType' : u'FR',
        'Validate' : u'模拟',
    }
    p = urllib.urlencode(chang_param_to_gb2312(_p))
    req = urllib2.Request(url, data=p)
    print urllib2.urlopen(req).read()
    #after process then change the file s name
    #os.rename(__file__, os.path.join(rename_path, 'over.py.bak'))
