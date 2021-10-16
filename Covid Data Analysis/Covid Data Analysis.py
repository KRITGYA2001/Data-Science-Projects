#!/usr/bin/env python
# coding: utf-8
Steps for beginners
1)Start With Smaller Datasets
2)Master Each Process In The Data Science Life Cycle
3)Learn To Draw Conclusions Through Visualization
4)Start Model Building After You Have Mastered Earlier Processes
# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


# In[36]:


file=pd.read_csv("covid_vaccine.csv")


# In[37]:


file.columns


# In[38]:


file.info


# In[39]:


print(file["State"].head())
print(file["State"].tail())


# In[40]:


data=pd.read_csv("covid_data.csv")


# In[41]:


data.head()


# In[42]:


data.columns


# In[43]:


data.tail()


# In[44]:


#to get the count,mean , std, min , max we use describe()
data.describe()


# In[45]:


data.isnull().sum()


# # Relating the variables with scatterplots

# In[47]:


#relation plot
sb.relplot(x="New deaths",y="New cases",data=data)


# In[48]:


sb.relplot(x="Recovered",y="Confirmed",data=data)


# In[50]:


sb.relplot(x="Recovered",y="Confirmed",hue="Deaths",data=data,palette="brg")

catplot is like scatter plot in seaborn
relplot is like the normal plot in seaborn
# In[54]:


data.columns


# In[62]:


sb.relplot(x="Confirmed",y="Deaths",kind='line',data=data)


# In[67]:


#catplot for catogerical data
sb.set()
sb.catplot(x="WHO Region",y="Active",data=data)


# In[74]:


sb.set()
sb.despine()
sb.distplot(data["Confirmed"])


# In[ ]:




