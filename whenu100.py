from datetime import datetime

a=str(input("who r u?"))
b=int(input("how old r u?"))
now=datetime.now()
print("{0} will be 100 year in {1}".format(a, now.year + 100 - b))