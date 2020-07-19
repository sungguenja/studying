read_f = open('data5.txt','r',encoding='utf-8')
write_f = open('db_song.txt','w',encoding='utf-8')

data = ''
for line, value in enumerate(read_f):
    if line%3 == 0:
        data += "insert into pages_song ('kr_title','jp_title','en_title') values " + '(' + "'" + value[:-1].replace("'","") + "'" + ","
    elif line%3 == 1:
        data += "'" + value[:-1].replace("'","") + "'" + ","
    else:
        data += "'" + value[:-1].replace("'","") + "'"  + "); \n"
        write_f.write(data)
        data=''