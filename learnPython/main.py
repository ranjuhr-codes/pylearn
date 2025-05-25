
# def choiceIf(choice):
#     color_dict = {1: "red", 2: "green", 3: "blue"}
#     return color_dict.get(choice, "white")
#
#
# print(choiceIf(3))
#
# for i in range(-10, 10):
#     print(i)
#
# print("letters------------------------------")
# for i in "Yadhunandana":
#     print(i)
#
# print("tuple------------------------------")
# for (first, second) in [(1, "one"), (2, "two"), (3, "three"), (4, "four")]:
#     print(first, second)
#     print(first)
#
# print("dict------------------------------")
# for (keys, values) in {1: "one", 2: "two", 3: "three", 4: "four"}.items():
#     print((keys, values))
#     print(keys)
#     print(values)

# def fPos(a,b,c):
#     print("keine default values",a,b,c)

# def fPos(a,b=2,c = 3):
#     print(a,b,c)
#
# fPos(c=3,b=2,a=1)

# def fTup(*args):
#     print (args)
# def fDict(**kargs):
#     print (kargs)
# def fPosTupDict(a, *pargs, **kargs):
#     print (a, pargs, kargs)
#
# fTup()
# fTup(1)
# fTup(1, 2, 3, 4)
# fDict()
# fDict(1)
# fPosTupDict(1, 2, 3, x = 1, y = 2)

# for val in map(lambda inVal: pow(2, inVal), range(-10, 10)): print(val)

# for val in filter(lambda inVal: inVal<0, range(-10, 10)): print(val)

# data= ['root', '0', 'bin', '1', 'daemon', '2', 'lp', '4', 'mail',
# '8', 'games', '12', 'wwwrun', '30','ftp', '40','nobody', '65534',
# 'irc', '39', 'at', '25']
# dataDict = dict(zip(data[0::2], data[1::2]))
# print(dataDict)

# for i in [2**x for x in range(0, 20) if x % 2 == 1]:
#     print("2**x", i)

# names = ["Rainer", "michaeL", "rAiner", "michaEl", "raIner", "MichAel"]
#
# nameDecorated = [(name.upper(), counter, name) for counter, name in enumerate(names)]
# nameDecorated.sort()
# print("Sorted case insensitive: ")
# print(nameDecorated)
#
# print("Sorted with stabil:")
# print([(counter, value) for name, counter, value in nameDecorated])
# print([value for _, _, value in nameDecorated])
#
# names.sort(key=lambda x: x.upper())
#
# print(names)

import sys
import source as temp
# from source import var
# from source import function
# from source import SimpleClass

# print(temp.__name__)
# print(sys.path)
# print(temp.var)
# temp.function()
# simpleClass = temp.SimpleClass()
# print(simpleClass.name())
#
# print(__name__)

# file1 = open("testfile1.txt","w+")
# file1.write("file1 data")
# file1.seek(0)
#
# data = file1.read()
# print(data)
# print(type(data))
#
# file2 = open("testfile2.txt", "w+")
#
# file2.write(data)
# file2.seek(0)
# print(file2.read())
#
# class HumanBeing(object):
#     def __init__(self, na):       # Implementation
#         self.__name = na          # Implementation
#     def getName(self):            # interface
#         return self.__name
#     def changeName(self, newName):# interface
#         self.__name = newName
#
# class Man(HumanBeing):
#     def getSex(self): return "male"
#
# class Woman(HumanBeing):
#     def getSex(self): return "female"
#
# def hasDifferentSex(fir, sec):
#     return fir.getSex() != sec.getSex()
#
# def marryUs(fir, sec):
#     if (hasDifferentSex(fir, sec)):
#         fir.changeName(fir.getName() + "-" +
#                        sec.getName())
#
# yadhu  = Man("Yadhu")
# akila = Woman("Akila")
#
# print("Before marriage")
# print(yadhu.getName())
# print(akila.getName())
#
# marryUs(akila, yadhu)
#
# print("After marriage")
# print(yadhu.getName())
# print(akila.getName())

# class Student:
#     number = 0
#
#     def __init__(self, n):
#         Student.number += 1
#         self.__name = n
#         self.setID(n + str(Student.number))  # Student.setID(self,str(n+Student.number))
#
#     def getNumber(self):
#         return Student.number
#
#     def setID(self, id):
#         self.__ID = id
#
#     def getID(self):
#         return self.__ID
#
#     def __del__(self):
#         Student.number -= 1
#
# class DesignStudent(Student):
#     def __init__(self, n):
#         Student.__init__(self, n)
#
#     def getID(self):
#         return "Designer: " + Student.getID(self)
#
# designStudent = DesignStudent("Guru")
#
# artStudent = Student("Yadhu")
#
# print(designStudent.getID())
# print(artStudent.getID())

import random


class Ball:
    def getName(self):
        return self.__class__.__name__


class Handball(Ball): pass
    # def getName(self):
    #     return self.__class__.__name__


class Basketball(Ball): pass
    # def getName(self):
    #     return self.__class__.__name__


for i in range(10):
    print(random.choice((Ball(), Handball(), Basketball())).getName())

