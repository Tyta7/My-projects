#!/usr/bin/env python
# coding: utf-8

# Data Loading 

# In[ ]:


import pandas as pd 


# In[2]:


nf = pd.read_csv("netflix_titles.csv")

nf.head(5)


# In[3]:


nf.tail(5)


# In[4]:


nf.info()
nf.shape


# Data Sorting and Cleaning

# In[5]:


sorted_nf = nf.sort_values('release_year', ascending = True, kind= 'heapsort', na_position= 'last')
sorted_nf.head()


# In[6]:


new_nf = sorted_nf.dropna()


# In[7]:


new_nf.head(5)


# In[8]:


new_nf.info()
new_nf.shape


# In[15]:


print(new_nf.duplicated())


# In[17]:


new_nf.drop_duplicates()


# Data Analysis

# In[10]:


print(new_nf.release_year.unique())
print(new_nf.release_year.nunique())
print(new_nf.release_year.mode())
new_nf.loc[new_nf.release_year == 2017]


# In[11]:


print(new_nf.title.describe())
print(new_nf.title.unique())


# In[12]:


print(new_nf.type.describe())

print(new_nf.type.unique())


# In[13]:


print(new_nf.rating.describe())
print(new_nf.rating.unique())


# In[14]:


new_nf.director.unique()
new_nf.director.describe()


# In[19]:


new_nf.cast.unique()
new_nf.cast.describe()


# In[20]:


new_nf.listed_in.describe()
