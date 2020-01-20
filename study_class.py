class Shape:
def __init__(self, length):
self.__length = length

def ar(self):
return self.__length * self.__length

def length(self):
return self.__length

class Squre(Shape):
def __init__(self, length, area):
super(Squre, self).__init__(length)
self.__area=area

def area(self):
return self.__area

def __repr__(self):
return "{0}".format(super(Squre, self).ar())

N1=Squre(3, 9)
print(N1)

class Person:
def __init__(self, gender):
self.__gender = gender

def gender(self):
return self.__gender

def __repr__(self):
return "{0}".format(self.__gender)

class Son(Person):
def __init__(self, gender):
super(Son, self).__init__(gender)

def __repr__(self):
return "{0}".format(super(Son, self).gender())

J1=Son("Male")
J2=Son("Female")
print(J1)
print(J2)