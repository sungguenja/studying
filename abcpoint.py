a="ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
b=list(a)
print(b)
z=0
x=0
c=0
v=0
for i in range (0,len(b)):
    if b[i]=='A':
        z+=1
    elif b[i]=='B':
        x+=1
    elif b[i]=='C':
        c+=1
    elif b[i]=='D':
        v+=1
print(4*z+3*x+2*c+v)