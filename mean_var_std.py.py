#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[6]:


def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
    else :
        array = np.array(list)
        A = array.reshape(3,3)
        B = np.transpose(A)
        calculations = {
            
          'mean': [np.mean(A, axis = 0), np.mean(B, axis=0), np.mean(array)],
          'variance': [np.var(A, axis = 0), np.var(B, axis = 0), np.var(array)],
          'standard deviation': [np.std(A, axis = 0), np.std(B, axis = 0), np.std(array)],
          'max': [np.max(A, axis = 0), np.max(B, axis = 0), np.max(array)],
          'min': [np.min(A, axis = 0), np.min(B, axis = 0), np.min(array)],
          'sum': [np.sum(A, axis = 0), np.sum(B, axis = 0), np.sum(array)]
        }
        return calculations
calculate([0,1,2,3,4,5,6,7,8,])


# In[ ]:





# In[ ]:




