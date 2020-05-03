import re
read_f = open('data1.txt','r',encoding='utf-8')
write_f = open('text2.txt','w',encoding='utf-8')

data = ''
for line, value in enumerate(read_f):
    if line>=652:
        break
    elif 7<line<652:
        if line%8==0:
            data += "insert into accounts_fish ('name','date','time','where','size','bell') values " + '(' + "'" + str(re.sub('[^가-힣]','',value)) + "'" + ','
        elif line%8==2:
            data += "'" + value[:-1] + "'" + ','
        elif line%8==3:
            data += "'" + value[:-1] + "'" + ','
        elif line%8==4:
            data += "'" + value[:-1] + "'" + ','
        elif line%8==5:
            data += "'" + value[:-1] + "'" + ','
        elif line%8==6:
            data += value[:-1] + ')' + ';' + '\n'
            write_f.write(data)
            data = ''