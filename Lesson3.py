#Python for loops
from unittest import result


fruits = ["apple","banana","cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

#range function
for x in range(6):#start from 0 to 5
    print(x) 

for x in range(2,8):#start from 2 to 7
    print(x)

# Nested loops
adj = ["red","big","tasty"]
fruits = ["apple","cherry","banana"]
for x in adj:
    for y in fruits:
        print(x ,y)

#python functions
def my_function():# creating a function
    print("Hello the other side of the World")
my_function() #calling a function

#python arguments
def my_function(fname):
    print(fname + " Murkepen")
my_function("Emmily")
my_function("sylvia")
my_function("Diana")    

#number of arguments
def my_function(fname,lname):
    print(fname + " " + lname)
my_function("Emmily", "Nabaala")   

#Arbitrary arguments, *args
def my_function(*kids):#if you do not know the number of arguments to be passed add *
    print("The youngest child is " + kids[2])
my_function("Emil","Tobias","Linus") 

#Arbitrary keyword Arguments, **kwargs
def my_function(**kid):#if you do not know how many keys to be passed into a function add **
    print("His last name is " + kid["lname"])
my_function(fname = "Tobias",lname ="Linus")   

#Default parameter value
def my_function(country = "Norway"):
    print(" I am from " + country)
my_function("Sweden")
my_function()
my_function("Brazil")    

#Return values
def my_function(x):
    return 3 * x
print(my_function(3))  
print(my_function(6)) 
print(my_function(9)) 

# Python Recursion
def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0  
    return result    
print("\n\nRecursion example result")
tri_recursion(3)   

#lambda
x = lambda a: a + 10
print(x(6))

y= lambda a,b: a * b
print(y(5, 6))

def my_function(n):
    return lambda a: a*n #"N"represents number of times to be double
mydoubler = my_function(2)
mytripler = my_function(3)
print(mydoubler(17)) 
print(mytripler(17))  

#Arrays in python
cars = ["ford","volve","BMW"]# creating an array
print(cars)
print(cars[0]) #accessing the elements of an array

#modify an array
cars = ["ford","Volve","BMW"]
cars[0] = "Toyota"# modifying
print(cars) 
print(len(cars))

#adding array elements
cars = ["ford","volve","BMW"]
cars.append("Honda")#adding an array
print(cars)

#removing an elemnt from an array
cars = ["potatoes","Tomatoes","Rice"]
cars.pop(1)
print(cars)
