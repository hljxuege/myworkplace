#encoding:utf-8
'''
Created on May 6, 2013

@author: liuxue
'''
# big intiger multiplication
def bigmul(a,b):
    sa = str(a)
    sb = str(b)
    resultline = ' '*(len(sa)+len(sb)) # len(a)+len(b) spaces
 
    #   a
    # * b
    print
    print resultline[:-len(sa)]+sa
    print '*'+resultline[:-len(sb)-1]+sb
 
    # ---
    print '-'*(len(sa)+len(sb))
 
    result_list = []  # result list, [b_i*a]
    cursp = 0   # spaces need to be added to the end, result shift postion
    for db in sb[::-1]:
        if int(db)==0: # b_i==0, result shift to right 1 postion
            cursp += 1
            continue
        else:
            result = '' # empty current result
            carrier = 0 # carrier from previous calculation
        for da in sa[::-1]: # b_i*a_i
            mr = int(db)*int(da)+carrier # result = b_i*a_i+carrier
            carrier = mr/10     # carrier = result /10
            result += str(mr%10)    # add last digit to the result
            if carrier!=0:       # process last carrier
                result += str(carrier)
            result = result[::-1]+' '*cursp   # reverse result string, add shift postion to the end
            cursp += 1         # add shift postion
            result_list.append(resultline[:-len(result)]+result) # append b_i*a to the result list
        print resultline[:-len(result)]+result  # print current result
         
        print '-'*(len(sa)+len(sb))
     
    # result
    print resultline[:-len(str(sum([int(x.replace(' ','0')) for x in result_list])))]+str(sum([int(x.replace(' ','0')) for x in result_list]))
     
# unit test
def main():
    a = 12345678900987654321
    b = 1234567009
 
    bigmul(b,a)
    bigmul(a,b)
 
if __name__=='__main__':
    main()