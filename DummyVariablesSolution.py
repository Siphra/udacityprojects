#!/usr/bin/env python
# coding: utf-8

# ### Dummy Variables
# 
# You saw in the earlier notebook that you weren't able to directly add a categorical variable to your multiple linear regression model.  In this notebook, you will get some practice adding dummy variables to your models and interpreting the output.
# 
# Let's start by reading in the necessary libraries and data.

# In[16]:


import numpy as np
import pandas as pd
import statsmodels.api as sm;
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

df = pd.read_csv('./house_prices.csv')
df.head()


# `1.` Use the [pd.get_dummies](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.get_dummies.html) documentation to assist you with obtaining dummy variables for the **neighborhood** column.  Then use [join](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.join.html) to add the dummy variables to your dataframe, **df**, and store the joined results in **df_new**.
# 
# Fit a linear model using **all three levels** of **neighborhood** neighborhood to predict the price. Don't forget an intercept.
# 
# Use your results to answer quiz 1 below.

# In[10]:


neighborhood_dummies = pd.get_dummies(df['neighborhood'])
df_new = df.join(neighborhood_dummies)
df_new.head()


# In[13]:


df_new['intercept'] = 1
lm = sm.OLS(df_new['price'], df_new[['intercept', 'A', 'B', 'C']])
results = lm.fit()
results.summary()


# `2.`  Now, fit an appropriate linear model for using **neighborhood** to predict the price of a home. Use **neighborhood A** as your baseline.  Use your resulting model to answer the questions in Quiz 2 and Quiz 3 below.

# In[14]:


lm2 = sm.OLS(df_new['price'], df_new[['intercept', 'B', 'C']])
results2 = lm2.fit()
results2.summary()


# `3.` Run the two cells below to look at the home prices for the A and C neighborhoods.  Add neighborhood B.  This creates a glimpse into the differences that you found in the previous linear model.

# In[30]:


plt.hist(df_new.query("C == 1")['price'], alpha = 0.3, label = 'C');
plt.hist(df_new.query("A == 1")['price'], alpha = 0.3, label = 'A');

plt.legend();


# `4.` Now, add dummy variables for the **style** of house, as well as **neighborhood**.  Use **ranch** as the baseline for the **style**.  Additionally, add **bathrooms** and **bedrooms** to your linear model.  Don't forget an intercept.  Use the results of your linear model to answer the last two questions below. **Home prices are measured in dollars, and this dataset is not real.**

# In[32]:


type_dummies = pd.get_dummies(df['style'])
df_new = df_new.join(type_dummies)
df_new.head()


# In[34]:


lm3 = sm.OLS(df_new['price'], df_new[['intercept', 'B', 'C', 'lodge', 'victorian', 'bedrooms', 'bathrooms']])
results3 = lm3.fit()
results3.summary()


# In[ ]:




