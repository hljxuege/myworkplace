#encoding:utf-8
'''
Created on May 2, 2013

@author: liuxue
@see: http://cloverprince.iteye.com/blog/464295
@note: 
    身份证校验码算法：
    设18位身份证号序列从左到右为: a[0], a[1], a[2], a[3], ..., a[16], a[17]
    其中a[i]表示第i位数字，i=0,1,2,...,17，如果最后一位（校验位）是X，则a[17]=10 
    每一位被赋予一个“权值”，其中，第i位的权值w[i]的计算方法是： w[i] = 2**(17-i) % 11
    
'''

chmap = {
    '0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
    'x':10,'X':10
    }

def ch_to_num(ch):
    return chmap[ch]    

def verify_string(s):
    char_list = list(s)
    num_list = [ch_to_num(ch) for ch in char_list]
    return verify_list(num_list)

def verify_list(l):
    sum = 0
    for ii,n in enumerate(l):
        weight = 2**(17 - ii) % 11
        sum = (sum + n*weight) % 11
        
    return sum==1
    
