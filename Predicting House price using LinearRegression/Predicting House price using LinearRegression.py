#!/usr/bin/env python
# coding: utf-8
Steps Involved In Predictive analysis
1)Data Exploration
2)Data Cleaning
3)Modeling
4)Performance Analysis
# # Data Exploration
Data exploration is basically understanding the data
no. of column
no. of rows
mean,std,min,max
# # Data Cleaning
Data cleaning is used to get rid of redundancies in the data.
removing/replace null values 
#    # Data Modeling
Model selection and building accounts for a very important part in predictive analysis.
find out the relation between the variables and then find out the prefect algo.
# # Performance Analysis
After building the model,the analysis of the model is necessary for efficiency.
Anything above 70% is good analysis.
# # Our task

# # Predictive Analysis Using Python
We will make a model to predict the price of a house from housing data.
# In[1]:


import pandas as pd
import seaborn as sb
import numpy as np
from sklearn.linear_model import LinearRegression


# In[2]:


data=pd.read_csv('house.csv')


# In[3]:


data.head()


# In[4]:


data.tail()


# In[5]:


data.columns


# In[6]:


data.shape


# In[7]:


data.describe()


# In[8]:


data.isnull().sum()


# In[10]:


#visulaization the data
#plots


# In[9]:


sb.pairplot(data)


# In[10]:


sb.relplot(x="price",y="bedrooms",data=data)


# In[11]:


sb.relplot(x="price",y="bathrooms",data=data)


# In[14]:


sb.relplot(x="price",y="sqft_living",data=data)


# In[12]:


sb.relplot(x="price",y="floors",data=data,hue="sqft_basement",palette="brg_r")


# In[13]:


sb.relplot(x="price",y="sqft_living",data=data,hue="bedrooms",palette="brg")


# In[ ]:


#modeling Part


# In[14]:


#for segregating the data
#Division of data into various categories for purposes of dividing 
#or restricting access to different classes of data.
from sklearn.model_selection import train_test_split


# In[15]:


data.head()


# In[29]:


#droping or removing the unwanter data from the file
train=data.drop(['price','date','street','city','sqft_lot','statezip','country','yr_built','yr_renovated'],axis=1)
test=data['price']


# In[17]:


test.head()


# In[18]:


train.head()


# In[19]:


X_train,X_test,y_train,y_test=train_test_split(train,test,test_size=0.4,random_state=2)


# In[20]:


print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)


# In[21]:


regr=LinearRegression()


# In[22]:


regr.fit(X_train,y_train)


# In[23]:


predict=regr.predict(X_test)


# In[24]:


predict


# In[25]:


regr.score(X_test,y_test)


# # Using testing data

# In[30]:


x=data[['bedrooms','bathrooms','sqft_living','floors','waterfront','view','condition','sqft_above','sqft_basement']]


# In[31]:


y=test


# In[32]:


test_data=[[3.0,1.50,1340,1.5,0,0,3,1340,0]]


# In[33]:


reg=LinearRegression()


# In[34]:


reg.fit(x,y)


# In[35]:


predict=reg.predict(test_data)


# In[36]:


print(predict)


# In[ ]:




