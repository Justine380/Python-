
from array import array
from typing import FrozenSet


print("hello Justine")

name = 'Murkepen'
print("My name is: ",name)
# Creating variable
age = 77
name = "justine"
print("my name is",name,"and I am ", age,"years")

# Casting in variable
x = str(23)
y = int(23)
z = float(23)
print(x)
print(y)
print(z)

#Getting the data type of a variable using type() function
a = 99
b = "Mayiani"
c = 39.0
print(type(a))
print(type(b))
print(type(c))

#case sensitive in Variable
a = 78
A = "Rachael"
print(a)
print(A)

 #value to multiple variable
x ,y ,z ="orange","cherry","apple"
print(x)
print(y)
print(z)

#unpacked list
fruits = ["Apple","Banana","Cherry"]
x ,y ,z = fruits
print(x)
print(y)
print(z)

#output variable
x = "python"
y = "is a programming"
z = "language"
print(x ,y ,z)

#Global variable
x = "awesome programming language mostly used "# global
def myfunc():
    x = "fantastic as it is easy to use" #creating a variable inside a function
    print("python is" ,x)

myfunc()
print("python is" ,x) 

#use the global keyword, the variable belongs to the global scope:
def myfunc():
    global x
    x = "fantastic"

myfunc()
print("python is a " + x)

#Data types
x = frozenset({"Ostrich","Flamingoes","Duck"}) #frozeset
print(x)

y = ["cattle", "sheep", "goat"] #list
print(y)

z = ("cattle", "sheep", "goat") #tuple
print(z)

a = {"fname":"Justine" ,"lname":"Murkepen","age":99} #dict
print(a)

#specified data types
x = str("Hello world")
print(x)
print(type(x))

#python number
x = 33e3
y = 25E4
z = -67.17e100
print(type(x))
print(type(y))
print(type(z))

#conversion
x = float(2)
y = int(3.9)
z = complex(2)
print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))


#muiltiline string
a = """ Python is awesome programming langauge ,
it is mostly used for coding. This is the ease language to be undestood by the programmers.
It is implemented for the creation of websites"""
print(a)

#string are arrays
a = "Hello , world!"
print(a[0])
print(a[-6])

#looping through a string
for x in "banana":
 print(x)

 #string length
 a = "Hello World!!!"
print(len(a))

#checking string
txt = "Keeping moving for the best life"
print( "yes 'best' is in txt")

#slicing string
y = "Justine Murkepen"
print(y[0:9])

#modify string
a = "Hello World"
print(a.upper())

#remove whitespace
a = " Justine Murkepen! "
print(a.strip())

#replace a string
x = "Hello World"
print(x.replace("H", "J"))

#string concatenation
x = "Blood"
y = "cells"
z = x + y
print(z)

#string format
age = 99
txt = "my name is Dr Java and I am {} years"
print(txt.format(age))