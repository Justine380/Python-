import pandas as pd
mydataset ={
    'cars':["BWM","Volve","Ford"],
    'passing':[3, 7, 2]
}
myvar = pd.DataFrame(mydataset)
print(myvar)

#pandas Series
import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)

#Create Labels
import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a, index =["x", "y","z"])
print(myvar)

#key/values objects as series
import pandas as pd
calories = {"day1":420,"day2":380,"day3":390,}
myvar = pd.Series(calories)
print(myvar)

#DATAFRAMES 
import pandas as pd
data = {
    "calories":[420, 380, 390],
    "duration":[50, 40, 45]
}
myvar = pd.DataFrame(data)
print(myvar)

#PANDAS DATFRAMES
import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data)#load data into a DataFrame object:
print(df.loc[0]) #to locates a row

#Loads Files into a DataFrame(READ CSV)
"""import pandas as pd
df = pd.read_csv('data.csv')
print(df.to_string())
#max_row
import pandas as pd
print(pd.options.display.max_rows) 
df = pd.read_csv('data.csv')
print(df)

#PANDAS Read JSON
import pandas as pd
df = pd.read_json('data.json')
print(df.to_string())"""
#Dictionary as JSON
import pandas as pd
data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)
print(df) 

#Analysing DataFrames
#Viewing the Data
import pandas as pd
df = pd.read_csv('data.csv')
print(df.head())