#encoding:utf-8
'''
Created on May 20, 2013

@author: liuxue
'''
import datetime
import urllib
import urllib2
RequestURL = 'http://dynamic.12306.cn/TrainQuery/iframeTrainInfoByCity.jsp'
c = ['train_code', 'from_station', 'to_station', 'date', 'time', 'arrive_date', 'arrive_time', 'cost_time', 'hard_seat', \
         'soft_seat', 'hard_sleep', 'soft_sleep', 'stage_one_seat', 'stage_two_seat', 'sepcial_seat', 'super_soft_seat', \
         'orign_station', 'dest_station', 'leavel', 'stop_by']
def query_train(from_station, to_station, date):

    p = {
            'nmonth4':'05',
            'nmonth4_new_value':'true',
            'nday4':'24',
            'nday4_new_value':'false',
            'fromtime':'任意时间',
            'fromtime_new_value':'true',
            'timerdo':'0',
            'timerdo_new_value':'false',
            'fromCityTrain':'北京',
            'fromCityTrain_new_value':'true',
            'trainTransCode':'',
            'trainTransCode_new_value':'true',
            'toCityTrain':'锦州',
            'toCityTrain_new_value':'true',
            'transCityTrain':'',
            'transCityTrain_new_value':'true',
            'nmonth6':'05',
            'nmonth6_new_value':'true',
            'nday6':'21',
            'nday6_new_value':'true',
            'transtime':'任意时间',
            'transtime_new_value':'false',
            'timerdo2':'0',
            'timerdo2_new_value':'false',
            'filterrdo':'1',
            'getsum':'3',
            'getsum_new_value':'true',
            'midstation1':'',
            'midstation2':'',
            'midstation3':'',
            'midstation4':'',
            'midstation5':'',
            'midstation6':'1',
            'midstation7':'',
            'midstation8':'',
            'midstation9':'',
            'k1':'0',
            'k2':'0',
            'k3':'0',
            'k4':'0',
            'k5':'0',
            'k6':'0',
            't1':'',
            't2':'',
            't3':'',
            't4':'',
            't5':'',
            't6':'',
            'date2':'',
            'date3':'',
            'date4':'',
            'date5':'',
            'date6':'',
            'ss':'3'
         }
    data = urllib.urlencode(p)
    req = urllib2.Request(RequestURL) 
    req.add_header("Cookie" , "JSESSIONID=6126393035A5A0302207404472832927; BIGipServerotsweb=2664694026.36895.0000; BIGipServertrainquery=2379809034.62495.0000; BIGipServerotsquery=2379809034.33825.0000" ) 
    req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    req.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3')
    req.add_header('Accept-Encoding', 'gzip,deflate,sdch')
    req.add_header('Accept-Language','en-US,en;q=0.8')
    req.add_header('Cache-Control','max-age=0')
    req.add_header('Connection','keep-alive')
    req.add_header('Content-Length','808')
    req.add_header('Content-Type','application/x-www-form-urlencoded')
    req.add_header('Cookie','JSESSIONID=6126393035A5A0302207404472832927; BIGipServerotsweb=2664694026.36895.0000; BIGipServertrainquery=2379809034.62495.0000; BIGipServerotsquery=2379809034.33825.0000')
    req.add_header('Host','dynamic.12306.cn')
    req.add_header('Origin','http://dynamic.12306.cn')
    req.add_header('Referer','http://dynamic.12306.cn/TrainQuery/TrainInfoByCity.jsp')
    req.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.22 (KHTML, like Gecko) Ubuntu Chromium/25.0.1364.160 Chrome/25.0.1364.160') 
        
    res = urllib2.urlopen(req, data) 
    html = res.read() 
    res.close()
    _tag = 'addRow'
    train_lines = []
    
    htmls = html.split('\n')
    for l in htmls:
        _location = l.find(_tag)
        if _location > 0:
            _left_ = l.find('\"') + 1
            _right_ = l.rfind('\"') 
            out_line = l[_left_: _right_]
            train_lines.append(out_line)
    
    return_trains = []
    for line in train_lines:
        return_line = []
        _l_3 = '' #出发日期
        _l_5 = '' #到达日期
        _l_7 = '' #历时
        _line = line.split(',')
        for item in _line[1:]:
            if item == '"+ardate+"':
                _add = ''
            _l = item.find('^')
            if _l > 0:
                _add = item[:_l]
            else:
                _add = item
                
            return_line.append(_add.strip())
            
        _l_3 = return_line[3]
        _l_7 = return_line[7]
        _date = datetime.datetime.strptime(_l_3, '%Y%m%d')
        h, m = tuple([int(i) for i in _l_7.split(':')])
        seconds = h*3600 + m*60 
        _need_date = _date + datetime.timedelta(seconds=seconds)
        _l_5 = _need_date.date().strftime('%Y%m%d')
        return_line[5] = _l_5
        return_trains.append(dict(zip(c, return_line)))
                                    
    return return_trains

if __name__ == '__main__':
    s = query_train('','','')
    for i in s:
        print i