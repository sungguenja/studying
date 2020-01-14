from datetime import datetime

a=str(input("who r u?"))
b=int(input("how old r u?"))
now=datetime.now()
print("{0}(은)는 {1}년에 100세가 될 것입니다.".format(a, now.year + 100 - b))