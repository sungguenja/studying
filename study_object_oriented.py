# class Student:

#     def __init__(self, name, gender, height):
#         self.__name = name
#         self.__gender = gender
#         self.__height = height

#     @property
#     def name(self):
#         return self.__name

#     @property
#     def gender(self):
#         return self.__gender

#     @property
#     def height(self):
#         return self.__height
    
#     @height.setter
#     def height(self, height):
#         self.__height = height

#     def __repr__(self):
#         return "{0}(name: {1}, gender: {2}, height: {3})".format(self.__class__.__name__, self.__name, self.__gender, self.__height)


# students = [
#     Student("mike", "M", 176.5),
#     Student("harry", "M", 182.5),
#     Student("elsa", "F", 157.2),
#     Student("jugnaut", "M", 183.6)
# ]

# for student in students:
#     print(student)

# print("Sorting by name")
# for student in sorted(students, key=lambda x: x.name):
#     print(student)
# print("Sorting reverse by name")
# for student in sorted(students, key=lambda x: x.name, reverse=True):
#     print(student)
# print("Sorting by height")
# for student in sorted(students, key= lambda x: x.height):
#     print(student)
# print("Sorting reverse by height")
# for student in sorted(students, key= lambda x: x.height, reverse= True):
#     print(student)

# class Student:

#     def __init__(self, kor, mat, eng):
#         self.__kor = kor
#         self.__mat = mat
#         self.__eng = eng

#     @property
#     def kor(self):
#         return self.__kor

#     @property
#     def mat(self):
#         return self.__mat

#     @property
#     def eng(self):
#         return self.__eng
    
#     @eng.setter
#     def height(self, eng):
#         self.__eng = eng

#     def __repr__(self):
#         return "국어, 영어, 수학의 총점: {0}".format(self.__kor + self.__mat + self.__eng)

# score = input().split(', ')
# s1=Student(int(score[0]),int(score[1]),int(score[2]))
# print(s1)

# class Nation:

#     def __init__(self, name, nation):
#         self.__name = name
#         self.__nation = nation
    
#     @property
#     def name(self):
#         return self.__name

#     @property
#     def nation(self):
#         return self.__nation
    
#     def __repr__(self):
#         return "ur name is {0} and nation is {1}".format(self.__name,self.__nation)

# u=input("input ur name and nation ex) ironman, USA").split(', ')
# m1=Nation(u[0], u[1])
# print(m1)

# class Student:
#     def __init__(self, name):
#         self.__name = name
    
#     @property
#     def name(self):
#         return self.__name
    
#     def shown(self):
#         print("name: {0}".format(self.__name))
    
#     def sh(self):
#         return "{0}".format(self.__name)

# class major(Student):
#     def __init__(self, name, maj):
#         super(major, self).__init__(name)
#         self.__maj=maj
    
#     @property
#     def major(self):
#         return self.__maj
    
#     def show(self):
        
#         print("name: {0}, major: {1}".format(super(major, self).sh(),self.__maj))

# s2=Student("mario")
# s3=major("link", "arrow")
# s2.shown()
# s3.show()

# class Circle:
#     def __init__(self, radius):
#         self.radius = int(radius)
    
#     def __repr__(self):
#         return "circle's area: {0}".format(3.14*self.radius**2)

# c1=Circle(2)
# print(c1)

# class area:
#     def __init__(self,hor,ver):
#         self.hor=int(hor)
#         self.ver=int(ver)
    
#     def __repr__(self):
#         return "Rectangle's area: {0}".format(self.hor*self.ver)

# hor1=int(input("pls input ur rectangle's horizon"))
# ver1=int(input("pls input ur rectangle's verticle"))
# r1=area(hor1,ver1)
# print(r1)

