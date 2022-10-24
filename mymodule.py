#Create a module
def greeting(name):
    print("Hello, " + name)

#use of module
import mymodule

mymodule.greeting("Jonathan")

#Variable in modules
person1 = {
    "name":"john", 
    "age":67,
    "country":"Norway"}
import mymodule
a = mymodule.person1["age"]
print(a)

#Built-in modules
import platform
x = platform.system()#identify the system
y = dir(platform)# list all defines names belonging to platform linux
print(x)
print(y)

#Import from a dictionary
def greeting(name):
    print("Hello, " + name)
person1 = {
    "name":"John",
    "age":35,
    "country":"Norway"
    }   
from mymodule import person1
print(person1["name"]) 
print(person1["age"])  
print(person1["country"])    

#Python Dates
import datetime
x = datetime.datetime.now()
print(x)

#Date Output
#The strftime() take one parameter,format to specify the format return string:
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))#return name of the week
print(x.strftime("%B"))#return name of the month
print(x.strftime("%D"))

#Creating date objects
import datetime
x = datetime.datetime(2022,12,22)
print(x)

#PYTHON MATH
#built-in math Function
x = min(2, 23,7,69)
y = max(2, 23,7,69)
print(x)
print(y)

#The abs() function
x = abs(-6.78)#return positive number
print(x)

#The power(x ,y) function
x = pow(2, 4)# same as (2*2*2*2)
print(x)

#The Math Module
import math
y = math.sqrt(81) # Return the square root of a number
print(y)

#The math ceil()
import math
x = math.ceil(1.4)
y = math.floor(1.4)
print(x)#return 2
print(y)#return 1

#The math.pi constant
import math
x = math.pi
print(x)

