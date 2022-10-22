#PYTHON CLASSES AND OJECTS
from email import iterators


class myclass:# creating a class
    x = 5
print(myclass)

#creating an object
class Myclass:
    x = 7
p1 = Myclass()#object 
print(p1.x)

#The __init__()function
class person:
    def __init__(self,name,age):# function
        self.name = name
        self.age =age
p1 = person("John",99)   
print(p1.name)
print(p1.age)    

#The __str__() function
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"
p1 = person("John",67)
print(p1)

#Objects methods
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myfunction(self):
        print("Hello my name is " + self.name)
p1 = person("James",58)            
p1.myfunction() 

#Create a PARENT class
class person:
    def __init__(self, fname ,lname):
        self.fname = fname
        self.lname = lname
    def printname(self):
        print(self.fname, self.lname)
x = person("Peter","Duncan")#use person class to create object
x.printname()

#Create a child class
class person:
    def __init__(self, fname ,lname):
        self.fname = fname
        self.lname = lname
    def printname(self):
        print(self.fname, self.lname)
class student(person):
    pass
x = student("Mike","Olsen") 
x.printname()       

#use the super() funcion
class person:
    def __init__(self, fname ,lname):
        self.fname = fname
        self.lname = lname
    def printname(self):
        print(self.fname, self.lname)
class student(person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)# inherit both methods&properties from the parent class
x = student("Mike","shadrack") 
x.printname()  

#Add methods
class person:
    def __init__(Ok,fname,lname):
        Ok.fname = fname
        Ok.lname = lname
    def myfunc(Ok):
        print(Ok.fname.Ok.lname)
class student(person):
    def __init__(Ok,fname,lname,year):
        super().__init__(fname,lname)
        Ok.graduationyear = year
    def welcome(Ok):# adding method welcome to this class student
        print("welcome", Ok.fname,Ok.lname,"to the class of", Ok.graduationyear)  
x = student("Justine","Murkepen", 2024)      
x.welcome()

#python iterators
mytuple = ("apple","banana","cherry")
myit = iter(mytuple)#return an iterator from a tuple
print(next(myit))
print(next(myit))
print(next(myit))

#create an iterator
class mynumbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x 
myclass = mynumbers()
myiter = iter(myclass)
print(next(myiter))  
print(next(myiter)) 
print(next(myiter)) 
print(next(myiter)) 
print(next(myiter))          

#stopiteration
class mynumbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
      if self.a <= 20:
         x = self.a
         self.a += 1
         return x 
      else:
       raise StopIteration 
myclass = mynumbers()
myiter = iter(myclass)
for x in myiter:
    print(x)

#Python scope
def myfunc():
    x = 300 #local variable
    def myinnerfunc():#function inside a function
        print(x)
    myinnerfunc()
myfunc()