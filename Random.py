#RANDOM NUMBERS IN NUMPY..
from importlib.metadata import distribution
from numpy import random
x = random.randint(100)
print(x)

#Generate randon Array
from numpy import random
x = random.randint(100, size=(3, 5))
print(x)

#Random Data Distribution
from numpy import random
x = random.choice([3, 5 ,6 ,9], p=[0.1, 0.3, 0.4,0.2], size=(3,5))
print(x)

#Random Permutations
from numpy import random
import numpy as np
arr = np.array([1, 2, 3, 4])
random.shuffle(arr)
print(arr)

#permutations
from numpy import random
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(random.permutation(arr))

#visualize Distribution with Seaborn
#ploting a distplot with a histogram
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot([0, 1, 2, 3, 4 ,5 ,6])
plt.show()

#plotting a displot without the Histogram
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot([0, 1, 2, 3, 4,])

#Visualization of the Normal Distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.normal(size=1000),hist=False)
plt.show()

#Binomial distribution
from numpy import random
x = random.binomial(n=10, p=0.5,size=10)
print(x)

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.binomial(n=10, p=0.5, size=1000),hist=True, kde=False)
plt.show()

#Poison Distribution
from numpy import random
x= random.poisson(lam=2,size=10)
print(x)
#Visualization of poison distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.histplot(random.poisson(lam=2,size=1000),kde=False)
plt.show()

#Uniform Distribution
from numpy import random
x= random.uniform(size=(2, 3))
#visualiztion of Uniform Distribtion
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.uniform(size=1000),hist=False)
plt.show()

#Logistics Distribution
from numpy import random
x= random.logistic(loc=1,scale=2,size=(2, 3))
print(x)
#visualization of Logistic Distribtion
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.logistic(size=1000),hist=False)
plt.show()

#Multinomial distribution
from numpy import random
x= random.multinomial(n=6,pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print(x)

#visualization of Exponential Distribution
from numpy import random
x= random.exponential(scale=2, size=(2,3))
print(x)
#visualization of exponential Distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.exponential(size=1000),hist=False)
plt.show()

#CHI Square Distribution
from numpy import random
x= random.chisquare(df=2, size=(2,3))
print(x)
#visualization of chi square Distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.chisquare(df=1,size=1000), hist=False)
plt.show()

