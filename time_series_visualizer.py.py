#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=True)
df["date"] = pd.to_datetime(df["date"])
df.set_index("date")


# In[2]:


df["year"] =  df["date"].dt.year
df["month"] =  df["date"].dt.month
import calendar
df['month'] = df['month'].apply(lambda x: calendar.month_name[x])
df = df[(df["value"] <= df["value"].quantile(0.975)) &
        (df["value"] >= df["value"].quantile(0.025))]


# In[3]:


df


# In[4]:


x = df["date"]
y = df["value"]
def draw_line_plot():
    plt.plot(x, y, "r")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xticks(rotation=45)
    plt.figure(figsize = (10,10))
    plt.show
    fig.savefig('line_plot.png')
    return fig
draw_line_plot()


# In[17]:


def draw_bar_plot():
    k = sns.barplot(x = "year" , y = "value", hue = "month" , hue_order=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], data = df)
    plt.legend(title = "Months")
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.figure(figsize = (20,10))
    sns.move_legend(k, 'upper left'), 
    fig.savefig('bar_plot.png')
    return fig
draw_bar_plot()


# In[6]:


df['month'] = df["date"].dt.month.apply(lambda x: calendar.month_abbr[x])
def draw_box_plot():
    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1,2,figsize=(13, 5))
    sns.boxplot(y = "value", x = "year", data = df, ax = ax[0] ) 
    ax[0].set(xlabel="Year", ylabel="Page Views", title="Year-wise Box Plot (Trend)" )
    sns.boxplot(y = "value", x = "month", data = df, ax = ax[1] , order=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    ax[1].set(xlabel="Month", ylabel="Page Views", title="Month-wise Box Plot (Seasonality)")
    plt.show
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
draw_box_plot()


# In[ ]:





# In[ ]:




