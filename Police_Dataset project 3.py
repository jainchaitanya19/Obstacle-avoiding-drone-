#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df=pd.read_csv('Police_Data.csv')


# In[4]:


df.head()


# # Q1) Remove the columns thats only contains missing values.

# In[10]:


df.drop('country_name',axis=1,inplace=True)


# In[11]:


df.drop('search_type',axis =1,inplace =True)


# # Q2) For speeding, were men or women stopped more often?

# In[12]:


df.head()


# In[24]:


df[df.violation=='Speeding'].driver_gender.value_counts()


# # Q3) Does gender affect who gets seached during a stop?

# In[28]:


df.head()


# In[34]:


for i,j in df.groupby('driver_gender'):
    print(f'{i} {j["search_conducted"].sum()}')


# In[36]:


a=df.groupby('driver_gender')['search_conducted']


# In[38]:


a.sum()


# # Q4)What is the mean stop_duration?
# 

# In[55]:


df.head()


# In[61]:


df['stop_duration'].fillna(7.9,inplace=True)


# In[62]:


df.head()


# In[63]:


df['stop_duration'].mean()


# # Q5) compare the age distribution for each violation.

# In[64]:


df.head()


# In[66]:


df.groupby('violation')['driver_age'].describe()


# In[ ]:




