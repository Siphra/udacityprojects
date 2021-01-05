#!/usr/bin/env python
# coding: utf-8

# ### Calculating Errors
# 
# Here are two datasets that represent two of the examples you have seen in this lesson.
# 
# One dataset is based on the parachute example, and the second is based on the judicial example. Neither of these datasets is based on real people.
# 
# Use the exercises below to assist in answering the quiz questions at the bottom of this page.

# In[3]:


import numpy as np
import pandas as pd

jud_data = pd.read_csv('judicial_dataset_predictions.csv')
par_data = pd.read_csv('parachute_dataset.csv')


# In[4]:


jud_data.head()


# In[5]:


par_data.head()


# `1.` Above, you can see the actual and predicted columns for each of the datasets.  Using the **jud_data**, find the proportion of errors for the dataset, and furthermore, the percentage of errors of each type.  Use the results to answer the questions in quiz 1 below.

# In[6]:


jud_data[jud_data['actual'] != jud_data['predicted']].shape[0]/jud_data.shape[0] # Number of errors


# In[7]:


jud_data.query("actual == 'innocent' and predicted == 'guilty'").count()[0]/jud_data.shape[0] # Type 1 errors


# In[8]:


jud_data.query("actual == 'guilty' and predicted == 'innocent'").count()[0]/jud_data.shape[0] # Type 2 errors


# In[9]:


# If everyone was predicted to be guilty, then every actual innocent 
# person would be a type I error.

# Type I = pred guilty, but actual = innocent
jud_data[jud_data['actual'] == 'innocent'].shape[0]/jud_data.shape[0]


# In[10]:


#If everyone has prediction of guilty, then no one is predicted inncoent
#Therefore, there would be no type 2 errors in this case

# Type II errs = pred innocent, but actual = guilty
0


# `2.` Above, you can see the actual and predicted columns for each of the datasets.  Using the **par_data**, find the proportion of errors for the dataset, and furthermore, the percentage of errors of each type.  Use the results to answer the questions in quiz 2 below.

# In[11]:


par_data[par_data['actual'] != par_data['predicted']].shape[0]/par_data.shape[0] # Number of errors


# In[12]:


par_data.query("actual == 'fails' and predicted == 'opens'").count()[0]/par_data.shape[0] # Type 1 errors


# In[13]:


par_data.query("actual == 'opens' and predicted == 'fails'").count()[0]/par_data.shape[0] # Type 2 errors


# In[14]:


# If every parachute is predicted to fail, what is the proportion
# of type I errors made?

# Type I = pred open, but actual = fail
# In the above situation since we have none predicted to open,
# we have no type I errors

0


# In[15]:


# If every parachute is predicted to fail, what is
# the proportion of Type II Errors made?  

# This would just be the total of actual opens in the dataset, 
# as we would label these all as fails, but actually they open

# Type II = pred fail, but actual = open
par_data[par_data['actual'] == 'opens'].shape[0]/par_data.shape[0]


# In[ ]:




