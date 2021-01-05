#!/usr/bin/env python
# coding: utf-8

# ### Model Diagnostics in Python
# 
# In this notebook, you will be trying out some of the model diagnostics you saw from Sebastian, but in your case there will only be two cases - either admitted or not admitted.
# 
# First let's read in the necessary libraries and the dataset.

# In[1]:


import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, precision_score, recall_score, accuracy_score
from sklearn.model_selection import train_test_split
np.random.seed(42)

df = pd.read_csv('./admissions.csv')
df.head()


# `1.` Change prestige to dummy variable columns that are added to `df`.  Then divide your data into training and test data.  Create your test set as 20% of the data, and use a random state of 0.  Your response should be the `admit` column.  [Here](http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html) are the docs, which can also find with a quick google search if you get stuck.

# In[2]:


df[['1','2','3','4']] = pd.get_dummies(df.prestige)


# `2.` Now use [sklearn's Logistic Regression](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) to fit a logistic model using `gre`, `gpa`, and 3 of your `prestige` dummy variables.  For now, fit the logistic regression model without changing any of the hyperparameters.  
# 
# The usual steps are:
# * Instantiate
# * Fit (on train)
# * Predict (on test)
# * Score (compare predict to test)
# 
# As a first score, obtain the [confusion matrix](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html).  Then answer the first question below about how well your model performed on the test data.

# In[8]:


df['intercept'] = 1
y = df.admit
X = df[['gre','gpa','1','2','3']]
X_train,X_test,y_train,y_test = train_test_split(X,y, test_size=.20,random_state=0)
lm = LogisticRegression()
lm.fit(X_train,y_train)
y_pred = lm.predict(X_test)
print(precision_score(y_test,y_pred))
print(recall_score(y_test,y_pred))
print(accuracy_score(y_test,y_pred))
confusion_matrix(y_test,y_pred)


# In[ ]:





# `3.` Now, try out a few additional metrics: [precision](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html), [recall](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html), and [accuracy](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html) are all popular metrics, which you saw with Sebastian.  You could compute these directly from the confusion matrix, but you can also use these built in functions in sklearn.
# 
# Another very popular set of metrics are [ROC curves and AUC](http://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html#sphx-glr-auto-examples-model-selection-plot-roc-py).  These actually use the probability from the logistic regression models, and not just the label.  [This](http://blog.yhat.com/posts/roc-curves.html) is also a great resource for understanding ROC curves and AUC.
# 
# Try out these metrics to answer the second quiz question below.  I also provided the ROC plot below.  The ideal case is for this to shoot all the way to the upper left hand corner.  Again, these are discussed in more detail in the Machine Learning Udacity program.

# In[ ]:





# In[ ]:





# In[ ]:





# In[26]:


### Unless you install the ggplot library in the workspace, you will 
### get an error when running this code!

from ggplot import *
from sklearn.metrics import roc_curve, auc
get_ipython().run_line_magic('matplotlib', 'inline')

preds = log_mod.predict_proba(X_test)[:,1]
fpr, tpr, _ = roc_curve(y_test, preds)

df = pd.DataFrame(dict(fpr=fpr, tpr=tpr))
ggplot(df, aes(x='fpr', y='tpr')) +    geom_line() +    geom_abline(linetype='dashed')


# In[ ]:




