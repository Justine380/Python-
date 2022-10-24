#Parse JSON -Convert from JSON to PYTHON
import json
x = '{"name":"John", "age": 36,"city":"New York"}'# some json
y = json.loads(x)#parse x
print(y["age"])#The result is a python dictionary

#Convert from PYTHON to JSON
import json
#a python dict
x = {
    "name":"James",
    "age":89,
    "city":"Nairobi"
    }
y = json.dumps(x)# convertion into JSON
print(y)   #the result is a json string 

#FORMAT the Results
#convert a python objects containing all the legal data types
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))

#ORDER THE RESULTS
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# sort the result alphabetically by keys:
print(json.dumps(x, indent=4, sort_keys=True))

#PYTHON RegEx
import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
    print("Yes! we have a match")
else:
    print("No match")   


#Try..Except..Else in PYTHON 
try:
    print("Hello Justine")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong") 

    #Python User Input
username = input("Enter username:")
print("My username is:" + username)  

#Python String Formatting
#string format()
price = 49
txt = "The price is {} dollars"
print(txt.format(price))
