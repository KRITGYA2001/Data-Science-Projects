#!/usr/bin/env python
# coding: utf-8
Credit Card Fraud Detection Using Machine Learning
In this project, we will make a Fraud Detection using Data Science
# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns


# In[2]:


data=pd.read_csv("creditcard.csv")


# In[3]:


data.head()


# In[4]:


data.tail()


# In[5]:


print(data.shape)   #output(rows,col)
print(data.ndim)


# In[6]:


fraud=data.loc[data['Class']==1]
nfraud=data.loc[data["Class"]==0]


# In[7]:


fraud.head()


# In[8]:


fraud.describe()


# In[9]:


sns.relplot(x="Amount",y="Time",hue="Class",data=data)


# In[13]:


from sklearn import linear_model
from sklearn.model_selection import train_test_split


# In[14]:


x=data.iloc[:,:-1]
y=data["Class"]


# In[20]:


X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.35)


# In[23]:


#Classifier
clf=linear_model.LogisticRegression(C=1e5)


# In[24]:


clf.fit(X_train,y_train)


# In[27]:


predict=clf.predict(X_test)
y_pred=np.array(clf.predict(X_test))
y=np.array(y_test)


# In[26]:


predict


# In[29]:


from sklearn.metrics import confusion_matrix,classification_report,accuracy_score


# In[30]:


#[true neg       ]
#[          False neg]
print(confusion_matrix(y_test,y_pred))


# In[32]:


print(accuracy_score(y_test,y_pred))


# In[33]:


print(classification_report(y_test,y_pred))


# In[34]:


print(accuracy_score(y_test,predict))


# In[37]:


print(classification_report(y,y_pred))


# In[ ]:




