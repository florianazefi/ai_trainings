import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

xx = np.linspace(0,1,200)   # start,stop,step
yy = np.sin(xx*2.*np.pi)

def f(x):
    """
    Function to return a sin function
    """
    return np.sin(x*2.*np.pi)

def g(x):
    """
    Function to add noise
    """
    return np.random.normal(loc=0.0, scale=0.1, size=n) 

n = 10
nn = 200
xx = np.linspace(0,1,nn)

x = np.linspace(0, 1, n)
y = f(x) + g(x)

p = np.polyfit(x,y,1) #pol fit 

plt.scatter(x,y)
plt.plot(xx,yy)
plt.plot(xx, np.polyval(p,xx))
#plt.xlim(0.,1)
#plt.ylim(-1.,1)
plt.show()
