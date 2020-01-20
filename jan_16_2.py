# a=input().split()
# print(a)
# a.reverse()
# print(a)
# print(' '.join(a))

# b=input().split("/")

# c=list(input())
# d=['>> ']
# if c==[]:
#     exit()
# i=0
# while i<len(c):
#     d.append(c[i].upper())
#     i+=1
# print(''.join(d))

# e=input().split()
# i=0
# j=1
# while i<len(e):
#     while j<len(e):
#         if e[i]==e[j]:
#             e.pop(j)
#         else:
#             j+=1
#     i+=1
#     j=i+1
# e.sort()
# print(','.join(e))

# f=list(map(str, input()))
# print(f)
# i=0
# while i<len(f):
#     if f[i] == '1' or f[i] == '2' or f[i] == '3' or f[i] == '4' or f[i] == '5' or f[i] == '6' or f[i] == '7' or f[i] == '8' or f[i] == '9' or f[i] == '0':
#         f.pop(i)
#     else:
#         i+=1
# print(''.join(f))

# members = [
#     {"name": "홍길동", "age": 20},
#     {"name": "이순신", "age": 45},
#     {"name": "강감찬", "age": 35}
# ]
# for member in members:
#     print("{0}\t{1}".format(member["name"], member["age"]))

# def create(name, age):
#     return {"name": name, "age": age}

# def to_str(person):
#     return "{0}\t{1}".format(person["name"],person["age"])

# members = [
#     create("홍길동", 20),
#     create("이순신", 45),
#     create("강감찬", 35)
# ]

# for member in members:
#     print(to_str(member))

class person:
    count = 0


    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        person.count += 1
        print("{0} 객체가 생성되었습니다.".format(self.__name))
    
    def __del__(self):
        print("{0} 객체가 제거되었습니다.".format(self.__name))
    
    def to_str(self):
        return "{0}\t{1}".format(self.__name,self.__age)
    
    @property
    def name(self):
        return self.__name
    
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0:
            raise TypeError("나이는 0이상의 값만 허용합니다.")
        self.__age = age
    
    @classmethod
    def get_info(cls):
        return "현재 person 클래스의 인스턴스는 총 {0} 개입니다.".format(cls.count)

people = [
    person("홍길동", 20),
    person("이순신", 45),
    person("강감찬", 35)
]
print("현재 person 클래스의 인스턴스는 총 {0} 개입니다.".format(person.count))
for member in people:
    print(member.to_str())
print(person.get_info())
# member = person()

# if isinstance(member, person):
#     print("member는 person의 인스턴스 클래스이다")

