#boolens
a = 67
b = 33
if b > a:
    print("yes b is greater than a")
else:
    print("b is not greater than a")

#evaluates two variable
x = "Universe"
y = 17
print(bool(x))
print(bool(y))


def myfunction():
    return True
if myfunction():
        print("Yes")
else:
        print("No")

#operators
a = 17
b = 5
print(a*b)
print(a+b)
print(a/b)
print(a-b)
print(a%b)# modules
print(a**b)#expontiation
print(a//b)#floor division

#lists
thislist = ["potatoes","tomatoes","rice","beans","chapo"]
print(thislist)
print(len(thislist))#length of list
print(type(thislist))#data type
print(thislist[1]) #access items
print(thislist[1:4]) #range of indexes

#To add item to the end of list use append
mylist = ["orange","cherry","banana","mango"]
mylist.append("kiwi") #add to the end of list
mylist.insert(1,"apple") #insert to a list
print(mylist)

mylist = ["orange","cherry","banana","mango"]
mylist.remove("mango")# remove from the list
mylist.pop(1)# remove specific object
print(mylist)

#loop through a list
mylist = ["orange","cherry","banana","mango"]
for x in mylist:
    print(x)

mylist = ["orange","cherry","banana","mango"]  
for x in range(len(mylist)):#loop through index
    print(mylist[1])

#list comprehension
birds = ["Dove","Ostrich","Duck","Flamingoes"]
newlist = []
for x in birds:
    if "e" in x:
        newlist.append(x) #creating a new list.
print(newlist)        

#sort a list
thislist = [37 ,25 ,100 ,6 ,93]
thislist.sort()
print(thislist)
#sort descending a list
thislist = ["Dove","Ostrich","Duck","Flamingoes", "mango", "kiwi"]
thislist.sort(reverse=True)
print(thislist)

#copy lists
thislist = ["Dove","Ostrich","Duck","Flamingoes", "mango", "kiwi"]
mylist = thislist.copy()
print(mylist)

#Dictionary
dict = {
    "brand":"Toyota",
    "model":"mustang",
    "year":1990
    }
print(dict)
print(dict["model"])#specified item

#IF..ELSE
a = 200
b = 88
if b > a:
    print(" b is greater than a")
elif a==b:
    print("a and b are equal")
else:
    print("a is greater than b")    

#while loops
# break statement
i = 1
while i < 10:
    print(i)
    if (i==4):
        break
    i += 1

#continue statement
i = 0
while i < 10:
    i += 1
    if(i == 5):
        continue
    print(i)

#The else statement
i = 1
while i < 10:
    print(i)
    i += 1
else: 
    print("i is no longer less than 10")   






