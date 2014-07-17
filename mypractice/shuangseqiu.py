#encoding:utf-8
'''
Created on Jul 17, 2014

@author: liuxue
'''
import urllib
url = 'http://baidu.lecai.com/lottery/draw/list/50?d=2014-01-01'
response = urllib.urlopen(url).read()

# locate tbody
pos1 = response.find('<tbody>')
pos2 = response.find('</tbody>')
s_table = response[pos1+7:pos2]
import re
qhs = re.findall(r'>(\d{7})</a>', s_table)
kjrqs = re.findall(r'>(\d{4}-\d{2}-\d{2})</td>', s_table)
r1s = re.findall(r'ball_1\">(\d{2})</span>', s_table)
r2s = re.findall(r'ball_2\">(\d{2})</span>', s_table)
l_qhs = qhs[::-1]
l_kjrqs = kjrqs[::-1]
l = r1s[::-1]
l2 = r2s[::-1]
rs_l = [[l_kjrqs.pop(), l_qhs.pop(), l.pop(), l.pop(), l.pop(), l.pop(), l.pop(), l.pop(), l2.pop()] for x in l]
assert len(qhs) == len(kjrqs) == len(r2s) == len(r1s)/6
print rs_l

