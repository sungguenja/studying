import re
read_f = open('data.txt','r',encoding='utf-8')
write_f = open('text.txt','w',encoding='utf-8')

data = ''
for line, value in enumerate(read_f):
    if line>=568:
        break
    elif 6<line<568:
        if line%7==0:
            data += "insert into accounts_bug ('name','date','time','where','bell') values " + '(' + "'" + str(re.sub('[^가-힣]','',value)) + "'" + ','
        elif line%7==2:
            data += "'" + value[:-1] + "'" + ','
        elif line%7==3:
            data += "'" + value[:-1] + "'" + ','
        elif line%7==4:
            data += "'" + value[:-1] + "'" + ','
        elif line%7==5:
            data += value[:-1] + ')' + ';' + '\n'
            write_f.write(data)
            data = ''