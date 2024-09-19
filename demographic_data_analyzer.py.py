#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
df = pd.read_csv("adult(in).csv")


# In[2]:


df.head()


# In[3]:


race = pd.Series([len(df.query('race == " White"')), len(df.query('race == " Black"')), len(df.query('race == " Other"')),
                  len(df.query('race == " Amer-Indian-Eskimo"')),
                  len(df.query('race == " Asian-Pac-Islander"'))], 
                 index = [" White", " Black", " Other", " Amer-Indian-Eskimo", " Asian-Pac-Isalander"])


# In[4]:


race


# In[10]:


df.query('sex == " Male"')["age"].mean()


# In[15]:


len(df.query('education == " Bachelors"'))/ len(df)


# In[21]:


len(df.query('(education == " Bachelors" | education == " Masters" | education == " Doctorate" ) & income == " >50K"'))


# In[19]:


len(df.query('education == " Bachelors" | education == " Masters" | education == " Doctorate"'))


# In[22]:


3486/7491


# In[25]:


len(df.query('not (education == " Bachelors" | education == " Masters" | education == " Doctorate") & income ==" >50K"'))/ len(df.query('not (education == " Bachelors" | education == " Masters" | education == " Doctorate") '))


# In[30]:


df["hours-per-week"].sort_values 
#13


# In[48]:


len(df[ (df["hours-per-week"] == 13) & (df["income"] == " >50K" )])/ len(df[ df["hours-per-week"] == 13 ])


# In[51]:


len(df.query( 'income == " >50K"'))


# In[66]:


list = [" United-States"," Cambodia"," England"," Puerto-Rico"," Canada"," Germany"," Outlying-US(Guam-USVI-etc)"," India"," Japan"," Greece"," South"," China"," Cuba"," Iran"," Honduras"," Philippines"," Italy"," Poland"," Jamaica"," Vietnam"," Mexico"," Portugal"," Ireland"," France"," Dominican-Republic"," Laos"," Ecuador"," Taiwan"," Haiti"," Columbia"," Hungary"," Guatemala"," Nicaragua"," Scotland"," Thailand"," Yugoslavia"," El-Salvador"," Trinadad&Tobago"," Peru"," Hong"," Holand-Netherlands"]
for item in list:
    print(len(df[(df["income"] == " >50K") & (df["native-country"] ==  item)]) )  
print(7171/7841)


# In[79]:


list = [" Prof-specialty"," Exec-managerial"," Sales"," Tech-support"," Transport-moving"," Other-service"]
for item in list:
      print(len(df[ (df["income"] == " >50K") & (df["native-country"] == " India") & (df["occupation"] == item)]))
#Prof-specialty #25


# In[76]:





# In[ ]:




