#!/usr/bin/env python
# coding: utf-8

# In[41]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy import stats


# In[26]:


df = pd.read_csv("medical_examination.csv")


# In[3]:





# In[27]:


df["BMI"] = df.weight /(df.height/100)**2
df["overweight"] = df["BMI"]>25
df["overweight"] = df["overweight"].astype(int)


# In[28]:


df["gluc"] = df["gluc"]>1
df["gluc"] = df["gluc"].astype(int)
df["cholesterol"] = df["cholesterol"]>1
df["cholesterol"] = df["cholesterol"].astype(int)
df


# In[48]:


def draw_cat_plot():
    df_cat = pd.melt(df, id_vars = ["cardio"],value_vars =["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])
    df_cat = df_cat.groupby(["cardio", "variable", "value"]).size().reset_index()
    df_cat = df_cat.rename( columns = {0: "total"})
    ax = sns.catplot(kind = "bar",hue = "value", x= "variable", y = "total", data = df_cat, col = "cardio")
    fig = ax.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# In[56]:


def draw_heat_map():
    df_heat = df[(df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))]
    corr = df_heat.corr()
    mask = np.triu(np.ones_like(corr, dtype = bool)) 
    fig, ax = plt.subplots(figsize=(16, 9))
    ax = sns.heatmap(corr, mask=mask, annot = True, square = True, fmt = "0.1f")
    fig.savefig('heatmap.png')
    return fig


# In[ ]:




