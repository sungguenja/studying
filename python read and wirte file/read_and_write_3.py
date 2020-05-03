import re
read_f = open('villagers.txt','r',encoding='utf-8')
write_f = open('text3.txt','w',encoding='utf-8')

species = ['dog','frog','Anteater','gorilla','cat','bear','wolf',
'squirrel','chicken','eagle','pig','horse','octopus','deer','lion','bird','cow','baby_bear','crocodile','sheep','goat','duck','monkey','mouse','kangaroo','eliphant','rhino','koala','ostrich','rabbit','penguin','hippo','hamster','tiger']
last = ['밥','헨리','설백','릴라','잭슨','캔디','모니카','미사키','오골','티파니','가논','리아나','멍무리','첼시','라이오넬','메들리','화자','미애','용남이','차둘','래미','덕근','델리','치즈','마리아','펑크스','뿔님이','코알','휘니','토비','크리미','데이빗','햄쥐']

data = "insert into accounts_villagers ('kr_name','jp_name','en_name','sex','birthday','character','species') values " + '('
name = ''
trigger = 0
for line, value in enumerate(read_f):
    if line%7==0:
        data += "'" + value[:-1] + "'" + ","
        name = value[:-1]
    elif line%7==6:
        data += "'" + species[trigger] + "'" + ')' + ';' + '\n'
        if name in last:
            trigger+=1
        write_f.write(data)
        data = "insert into accounts_villagers ('kr_name','jp_name','en_name','sex','birthday','character','species') values " + '('
    else:
        data += "'" + value[:-1] + "'" + ","