#encoding:utf-8
'''
Created on Apr 28, 2013

@author: liuxue
'''
'''
原来的天朝良民证是15位，构成如下：
1～6位：地址码。采用的是行政区划代码，可以去统计局的网站查。
7～12位：生日期码。构成为yymmdd。
13～15位：顺序码。每个地区出生人口按顺序递增，最后一位奇数分给男的，偶数分给女的。

18位则有2点改动：
1.生日期码变为8位，构成为yyyymmdd。
2.增加校验码，即第18位。按照ISO 7064:1983.MOD 11-2校验码计算。

计算方法很无聊：
将身份证号码的前17位数分别乘以不同的系数。从第一位到第十七位的系数分别为：7 9 10 5 8 4 2 1 6 3 7 9 10 5 8 4 2 
将这17位数字和系数相乘的结果相加。
用加出来和除以11，得到余数。
余数的结果只可能为0 1 2 3 4 5 6 7 8 9 10这11种，分别对应的最后一位身份证的号码为1 0 X 9 8 7 6 5 4 3 2。
'''
import datetime
def _simple_verity_15(str_id):
    s6_12 = str_id[6:12]
    print datetime.datetime.strptime(s6_12, '%y%m%d')
    print s6_12
    
def _simple_verity_18(str_id):
    s6_14 = str_id[6:14]
    print datetime.datetime.strptime(s6_14, '%Y%m%d')
    print s6_14

def simple_id_verify(str_id):
    len_id  = len(str_id)
    len_status = (len_id == 15) or (len_id == 18)
    assert len_status, '身份证长度不合法'
    if len_id == 15:
        _simple_verity_15(str_id)
    elif len_id == 18:
        _simple_verity_18(str_id)
    
if __name__ == '__main__':
    simple_id_verify('232302890123131')
        