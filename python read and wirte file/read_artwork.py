read_f = open('artwork.txt','r',encoding='utf-8')
write_f = open('db_artwork.txt','w',encoding='utf-8')

data = ''
for line, value in enumerate(read_f):
    if line%3 == 0:
        data += "insert into pages_artwork ('title','original','fake') values " + '(' + "'" + value[:-1] + "'" + ","
    elif line%3 == 1:
        data += "'" + value[:-1] + "'" + ","
    else:
        if value[:-1] == '가품 없음':
            data += "0"
        else:
            data += "1"
        data += ')' + ';' + '\n'
        write_f.write(data)
        data=''