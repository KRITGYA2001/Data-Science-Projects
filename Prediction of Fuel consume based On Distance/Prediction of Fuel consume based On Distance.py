#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


# In[27]:


file=pd.read_csv("carsample.csv")


# In[28]:


x=file["distance"].values[:,np.newaxis]
y=file["consume"].values


# In[29]:


lst=LinearRegression()
lst.fit(x,y)


# In[30]:


test_values=[[11],[12],[13],[14],[15]]
values=lst.predict(test_values)
print(values)

