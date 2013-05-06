#encoding:utf-8
'''
Created on May 6, 2013

@author: liuxue
'''
# big intiger multiplication
def bigmul(a,b):
    sa = str(a) #做为乘数
    sb = str(b) #作为被乘数
    move_num = 0 #移位计数
    
    resultline = list('0'*(len(sa)+len(sb))) #出初始化结果队列
    resultline = [int(i) for i in resultline]
    mutied_a = sa[::-1]
    mutied_b = sb[::-1]
    
    for mb in mutied_b:
        _move_num = move_num
        for ma in mutied_a:
            r = int(mb) * int(ma)
            resultline[_move_num] = r + resultline[_move_num]
            
            _move_num = _move_num + 1
        move_num = move_num + 1
    
    _resultline = [int(i) for i in list('0'*(len(sa)+len(sb)))]
    _resultline.append(0)
    count = 0
    for r in resultline[:]:#处理队列中的数据
        sum = _resultline[count] + r
        _resultline[count] = sum%10
        _resultline[count+1] = sum/10 + _resultline[count+1]
        count = count + 1
    return _resultline
 
     
# unit test
def main():
    a = 12345678900987654321
    b = 1234567009
 
    print ''.join(str(i)for i in bigmul(b,a)[::-1]).lstrip('0')
    print ''.join(str(i)for i in bigmul(a,b)[::-1]).lstrip('0')
    print 12345678900987654321*1234567009
if __name__=='__main__':
    main()