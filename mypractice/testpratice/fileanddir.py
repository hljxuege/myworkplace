#encoding:utf-8
if __name__ == '__main__':
    import os
    dir_name = 'airticket_front'
    files = os.listdir(dir_name)
    errors = []
    for i in files:
        with open(os.path.join(dir_name, i), 'r') as fr:
            for l in fr:
                if l.find('ErrorInfo_1_0') > 0:
                    errors.append(l)

    for e in errors:
        with open('errors.txt', 'w') as fw:
            fw.write(e)
            fw.write('\n')