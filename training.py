a=['A','A','A','O','B','B','O','AB','AB','O']
x=0
y=0
z=0
m=0
for i in range(0,10,1):
    if str(a[i])=='A':
        x+=1
    elif str(a[i])=='B':
        y+=1
    elif str(a[i])=='O':
        z+=1
    elif str(a[i])=='AB':
        m+=1
print("'A':{0}, 'O':{1}, 'B':{2}, 'AB':{3}".format(x,z,y,m))