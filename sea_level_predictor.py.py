#!/usr/bin/env python
# coding: utf-8

# In[21]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy import stats


# In[50]:


df = pd.read_csv('epa-sea-level.csv')
df = df.dropna(subset =["CSIRO Adjusted Sea Level"])


# In[64]:


y = df["CSIRO Adjusted Sea Level"]
x = df["Year"]
xv = df.query('Year >= 2000')["Year"]
yv = df.query('Year >= 2000')["CSIRO Adjusted Sea Level"]
k = np.linspace(1880, 2050, 10000)
plt.scatter(x,y)
plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")
plt.title("Rise in Sea Level")
res1 = stats.linregress(x, y) 
res2 = stats.linregress(xv, yv)
plt.plot(k, res1.intercept + res1.slope*k, label='line of best fit 1')
plt.plot(k, res2.intercept + res2.slope*k, label='line of best fit 2')
plt.xlim(1880, 2060)
plt.ylim(-1, 15)


# In[61]:





# In[ ]:





# In[ ]:




