#!/usr/bin/env python
# coding: utf-8

# ## Analyze A/B Test Results
# 
# You may either submit your notebook through the workspace here, or you may work from your local machine and submit through the next page.  Either way assure that your code passes the project [RUBRIC](https://review.udacity.com/#!/projects/37e27304-ad47-4eb0-a1ab-8c12f60e43d0/rubric).  **Please save regularly.**
# 
# This project will assure you have mastered the subjects covered in the statistics lessons.  The hope is to have this project be as comprehensive of these topics as possible.  Good luck!
# 
# ## Table of Contents
# - [Introduction](#intro)
# - [Part I - Probability](#probability)
# - [Part II - A/B Test](#ab_test)
# - [Part III - Regression](#regression)
# 
# 
# <a id='intro'></a>
# ### Introduction
# 
# A/B tests are very commonly performed by data analysts and data scientists.  It is important that you get some practice working with the difficulties of these 
# 
# For this project, you will be working to understand the results of an A/B test run by an e-commerce website.  Your goal is to work through this notebook to help the company understand if they should implement the new page, keep the old page, or perhaps run the experiment longer to make their decision.
# 
# **As you work through this notebook, follow along in the classroom and answer the corresponding quiz questions associated with each question.** The labels for each classroom concept are provided for each question.  This will assure you are on the right track as you work through the project, and you can feel more confident in your final submission meeting the criteria.  As a final check, assure you meet all the criteria on the [RUBRIC](https://review.udacity.com/#!/projects/37e27304-ad47-4eb0-a1ab-8c12f60e43d0/rubric).
# 
# <a id='probability'></a>
# #### Part I - Probability
# 
# To get started, let's import our libraries.

# In[36]:


import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
#We are setting the seed to assure you get the same answers on quizzes as we set up
random.seed(42)


# `1.` Now, read in the `ab_data.csv` data. Store it in `df`.  **Use your dataframe to answer the questions in Quiz 1 of the classroom.**
# 
# a. Read in the dataset and take a look at the top few rows here:

# In[37]:


#read in raw data
df = pd.read_csv('ab_data.csv')
df.head()


# b. Use the cell below to find the number of rows in the dataset.

# In[38]:


df.info() #confirming there are no missing or broken data sets and counting rows


# c. The number of unique users in the dataset.

# In[39]:


df.nunique() # identification of duplicate users


# d. The proportion of users converted.

# In[40]:


sum(df.converted)/df.user_id.nunique() #p converted overall


# e. The number of times the `new_page` and `treatment` don't match.

# In[41]:


#produces a dataframe containing any case where treatment = old and control = new
dfchk = df[df['group']== 'treatment']
dfchkop = df[df['group'] == 'control']
dfchk = dfchk[dfchk['landing_page']== 'old_page']
dfchkop = dfchkop[dfchkop['landing_page'] == 'new_page']
dfchk = dfchk.append(dfchkop)
dfchk.info()


# f. Do any of the rows have missing values?

# In[42]:


#no


# `2.` For the rows where **treatment** does not match with **new_page** or **control** does not match with **old_page**, we cannot be sure if this row truly received the new or old page.  Use **Quiz 2** in the classroom to figure out how we should handle these rows.  
# 
# a. Now use the answer to the quiz to create a new dataset that meets the specifications from the quiz.  Store your new dataframe in **df2**.

# In[43]:


#drops the rows with questionable data
df2 = df[~df.isin(dfchk)].dropna()
df2.head()


# In[44]:


# Double Check all of the correct rows were removed - this should be 0
df2[((df2['group'] == 'treatment') == (df2['landing_page'] == 'new_page')) == False].shape[0]


# `3.` Use **df2** and the cells below to answer questions for **Quiz3** in the classroom.

# a. How many unique **user_id**s are in **df2**?

# In[45]:


#identifies any duplicated users or rows in our dataframe
df2.nunique()


# b. There is one **user_id** repeated in **df2**.  What is it?

# In[46]:


#locates duplicated user
dups = df2[df2.user_id.duplicated(keep = False)==True]
dups


# c. What is the row information for the repeat **user_id**? 

# In[47]:


1899,2893


# d. Remove **one** of the rows with a duplicate **user_id**, but keep your dataframe as **df2**.

# In[48]:


#dropping duplicate user row, this could be done randomly due to the user not converting in either case
#more care would be required in the case of a user converting once, but not the other time.
df2.drop(2893, axis=0, inplace=True)
df2.shape


# `4.` Use **df2** in the cells below to answer the quiz questions related to **Quiz 4** in the classroom.
# 
# a. What is the probability of an individual converting regardless of the page they receive?

# In[49]:


#conversion probability
conv = sum(df2.converted)/df2.shape[0]


# b. Given that an individual was in the `control` group, what is the probability they converted?

# In[50]:


#control conversion probability and control dataframe 
dfc = df2[df2.group == 'control']
conv_c = sum(dfc.converted)/dfc.shape[0]
conv_c


# c. Given that an individual was in the `treatment` group, what is the probability they converted?

# In[51]:


#treatment conversion probability and creation of treatment dataframe
dft = df2[df2.group == 'treatment']
conv_t = sum(dft.converted)/dft.shape[0]
conv_t


# d. What is the probability that an individual received the new page?

# In[52]:


sum(df2.group == 'treatment')/df2.shape[0] # probability of a user being in treatment group


# e. Consider your results from parts (a) through (d) above, and explain below whether you think there is sufficient evidence to conclude that the new treatment page leads to more conversions.

# There is insufficient evidence to reject the null for this case. Assuming that the null is defined as the old page performing as well as or better than the new design. In our sample the old page actually did out perform the new page, but we have not yet determined the statistical significance of that.

# <a id='ab_test'></a>
# ### Part II - A/B Test
# 
# Notice that because of the time stamp associated with each event, you could technically run a hypothesis test continuously as each observation was observed.  
# 
# However, then the hard question is do you stop as soon as one page is considered significantly better than another or does it need to happen consistently for a certain amount of time?  How long do you run to render a decision that neither page is better than another?  
# 
# These questions are the difficult parts associated with A/B tests in general.  
# 
# 
# `1.` For now, consider you need to make the decision just based on all the data provided.  If you want to assume that the old page is better unless the new page proves to be definitely better at a Type I error rate of 5%, what should your null and alternative hypotheses be?  You can state your hypothesis in terms of words or in terms of **$p_{old}$** and **$p_{new}$**, which are the converted rates for the old and new pages.

# **The null hypothesis in this case is the the old page is better than or equal to the new page N0 >= N1 The alternative hypothesis in this case is the new page is better than the old page N1 > N0
# **

# `2.` Assume under the null hypothesis, $p_{new}$ and $p_{old}$ both have "true" success rates equal to the **converted** success rate regardless of page - that is $p_{new}$ and $p_{old}$ are equal. Furthermore, assume they are equal to the **converted** rate in **ab_data.csv** regardless of the page. <br><br>
# 
# Use a sample size for each page equal to the ones in **ab_data.csv**.  <br><br>
# 
# Perform the sampling distribution for the difference in **converted** between the two pages over 10,000 iterations of calculating an estimate from the null.  <br><br>
# 
# Use the cells below to provide the necessary parts of this simulation.  If this doesn't make complete sense right now, don't worry - you are going to work through the problems below to complete this problem.  You can use **Quiz 5** in the classroom to make sure you are on the right track.<br><br>

# a. What is the **conversion rate** for $p_{new}$ under the null? 

# In[53]:


conv #the p vaules under the assumptions laid out above


# b. What is the **conversion rate** for $p_{old}$ under the null? <br><br>

# In[54]:


conv


# c. What is $n_{new}$, the number of individuals in the treatment group?

# In[55]:


dft.shape[0] # for both n_new and n_old, the number of rows = number of unique users


# d. What is $n_{old}$, the number of individuals in the control group?

# In[56]:


dfc.shape[0] 


# e. Simulate $n_{new}$ transactions with a conversion rate of $p_{new}$ under the null.  Store these $n_{new}$ 1's and 0's in **new_page_converted**.

# In[57]:


#random choice used to produce p_new and p_old, random binomial could also have been used.
new_page_converted = np.random.choice([0,1], dft.shape[0],replace= True, p=[1 - conv,conv])
p_new = new_page_converted.mean()


# f. Simulate $n_{old}$ transactions with a conversion rate of $p_{old}$ under the null.  Store these $n_{old}$ 1's and 0's in **old_page_converted**.

# In[58]:


old_page_converted = np.random.choice([0,1], dfc.shape[0], replace= True, p=[1 - conv, conv])
p_old = old_page_converted.mean()


# g. Find $p_{new}$ - $p_{old}$ for your simulated values from part (e) and (f).

# In[59]:


#our random production of differences in probability
p_new-p_old


# h. Create 10,000 $p_{new}$ - $p_{old}$ values using the same simulation process you used in parts (a) through (g) above. Store all 10,000 values in a NumPy array called **p_diffs**.

# In[60]:


#bootstrap sampling of our binomial and calculation of the p_diffs array
nsamp = np.random.binomial(dft.shape[0], conv, 10000)/dft.shape[0]
osamp = np.random.binomial(dfc.shape[0], conv, 10000)/dfc.shape[0]
p_diffs = nsamp - osamp


# i. Plot a histogram of the **p_diffs**.  Does this plot look like what you expected?  Use the matching problem in the classroom to assure you fully understand what was computed here.

# In[61]:


plt.hist(p_diffs) #histogram of p


# j. What proportion of the **p_diffs** are greater than the actual difference observed in **ab_data.csv**?

# In[62]:


# calculate the p
p = (p_diffs > (conv_t - conv_c)).mean()
p


# k. Please explain using the vocabulary you've learned in this course what you just computed in part **j.**  What is this value called in scientific studies?  What does this value mean in terms of whether or not there is a difference between the new and old pages?

# **In part 'j.' of the project we determined the actual p-value for determining if our actual data allowed to us to reject the null hypothesis. In this case, with a p-value of 0.91 we must say that we can not reject the null for this case. **

# l. We could also use a built-in to achieve similar results.  Though using the built-in might be easier to code, the above portions are a walkthrough of the ideas that are critical to correctly thinking about statistical significance. Fill in the below to calculate the number of conversions for each page, as well as the number of individuals who received each page. Let `n_old` and `n_new` refer the the number of rows associated with the old page and new pages, respectively.

# In[63]:


#produce raw data for z_test
import statsmodels.api as sm
convert_old = sum(dfc.converted)
convert_new = sum(dft.converted)
n_old = dfc.shape[0]
n_new = dft.shape[0]


# m. Now use `stats.proportions_ztest` to compute your test statistic and p-value.  [Here](https://docs.w3cub.com/statsmodels/generated/statsmodels.stats.proportion.proportions_ztest/) is a helpful link on using the built in.

# In[64]:


# This is a z-score test
from statsmodels.stats.proportion import proportions_ztest as pzt
pzt([convert_old, convert_new], [n_old,n_new], alternative = 'smaller')


# n. What do the z-score and p-value you computed in the previous question mean for the conversion rates of the old and new pages?  Do they agree with the findings in parts **j.** and **k.**?

# **The z-score is how far removed from the mean of a normal distribution the data is, in our case barely over 1.3 SD away, meaning it falls in the 95% area of the normal distribution, as the p-value is >> .05 it agrees with the above probability of finding the values outside the expected normal distribution and supports further that we can not reject the null hypothesis in this case. Also notice the P of .905 agrees within 2 significant figures with our above calculated p of .903**

# <a id='regression'></a>
# ### Part III - A regression approach
# 
# `1.` In this final part, you will see that the result you achieved in the A/B test in Part II above can also be achieved by performing regression.<br><br> 
# 
# a. Since each row is either a conversion or no conversion, what type of regression should you be performing in this case?

# **Logistic Regression should be used, this is not a continuous distribution but a binary "yes/no"**

# b. The goal is to use **statsmodels** to fit the regression model you specified in part **a.** to see if there is a significant difference in conversion based on which page a customer receives. However, you first need to create in df2 a column for the intercept, and create a dummy variable column for which page each user received.  Add an **intercept** column, as well as an **ab_page** column, which is 1 when an individual receives the **treatment** and 0 if **control**.

# In[65]:


# creates a dataframe column to perform regression with, locating those users who got the new page
df2['ab_page']= np.where(df2.group == 'treatment',1,0)
df2['intercept'] = 1
df2.head()


# c. Use **statsmodels** to instantiate your regression model on the two columns you created in part b., then fit the model using the two columns you created in part **b.** to predict whether or not an individual converts. 

# In[66]:


# I determined a logistic regression best, as this is not a continuous variable
logmod = sm.Logit(df2['converted'],df2[['intercept','ab_page']])
results = logmod.fit()


# d. Provide the summary of your model below, and use it as necessary to answer the following questions.

# In[67]:


# provides results from our Logit
results.summary2()


# e. What is the p-value associated with **ab_page**? Why does it differ from the value you found in **Part II**?<br><br>  **Hint**: What are the null and alternative hypotheses associated with your regression model, and how do they compare to the null and alternative hypotheses in **Part II**?

# **The p-value associated with this model is .1899, significantly above .05 and shows us again that we cannot reject the null hypothesis. This differs from our previous method, which gave a .49 The difference being that in our previous work our null was that the the old page is better than or equal to, where as in this case our null was only that the old page is equal to, so any variation would reduce the p-value. There is statistically insignificant data suggesting that the new page may actually be worse than the old. **

# f. Now, you are considering other things that might influence whether or not an individual converts.  Discuss why it is a good idea to consider other factors to add into your regression model.  Are there any disadvantages to adding additional terms into your regression model?

# **Given the limited data set, we might look at time of day, to see if there were more converts during certain "time gates" at which people who were engaged with the pages might actually 'convert'. However, if we could obtain better data sets, with more detailed information, such as time on page, or location quick examples, we might be able to better predict who will and won't 'convert'. **

# g. Now along with testing if the conversion rate changes for different pages, also add an effect based on which country a user lives in. You will need to read in the **countries.csv** dataset and merge together your datasets on the appropriate rows.  [Here](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.join.html) are the docs for joining tables. 
# 
# Does it appear that country had an impact on conversion?  Don't forget to create dummy variables for these country columns - **Hint: You will need two columns for the three dummy variables.** Provide the statistical output as well as a written response to answer this question.

# In[68]:


# At this point we are adding in location variable to determine if location has had any impact
df_countries = pd.read_csv('countries.csv')
df2['user_id'] = df2.user_id.astype(int, inplace= True)
df3 = df2.merge(df_countries, on = 'user_id', how= 'left')
df3[['CA','UK','US']] = pd.get_dummies(df3.country)
# Running logit regression on the locations
logmod2 = sm.Logit(df3['converted'],df3[['intercept','CA','UK']])
results2 = logmod2.fit()
results2.summary2()


# **We can see from the above information that even any given nation doesn't have a specific impact on if anyone converts or not, ie, we can not reject the null, with the best p-val being above our .05 threshold.**

# h. Though you have now looked at the individual factors of country and page on conversion, we would now like to look at an interaction between page and country to see if there significant effects on conversion.  Create the necessary additional columns, and fit the new model.  
# 
# Provide the summary results, and your conclusions based on the results.

# In[69]:


#For interactions between location and new_page we've set up 3 new columns, though only 2 are required I 
#wanted to explor how they change.
df3['CA_c'] = df3.CA * df3.ab_page
df3['UK_c'] = df3.UK * df3.ab_page
df3['US_c'] = df3.US * df3.ab_page
df3.head()
# Logistic regression and summary 
logmod3 = sm.Logit(df3.converted, df3[['intercept','CA','US', 'CA_c', 'US_c']])
results3 = logmod3.fit()
results3.summary2()


# ** Once again even with this additional data that we find that we can not reject the null hypothesis that our original page is at least as good as our new page. **

# ** Overall Conclusions ** 
# 
# Our data was fairly consistently analyzed using the different methods, and while the p-values did fluctuate a tiny bit, we can be fairly certain the new page is not better than the original page in gaining conversions.  Other p-values were generally consistent around .9 and our z-score (~1.31) says our data point is well within the 95% area surrounding the mean for our normal distribution, providing further evidence that we can not reject the null hypothesis in this case, where our null hypothesis is that the old page is better than or equal to the new page. 
# 
# 
# 

# <a id='conclusions'></a>
# ## Finishing Up
# 
# > Congratulations!  You have reached the end of the A/B Test Results project!  You should be very proud of all you have accomplished!
# 
# > **Tip**: Once you are satisfied with your work here, check over your report to make sure that it is satisfies all the areas of the rubric (found on the project submission page at the end of the lesson). You should also probably remove all of the "Tips" like this one so that the presentation is as polished as possible.
# 
# 
# ## Directions to Submit
# 
# > Before you submit your project, you need to create a .html or .pdf version of this notebook in the workspace here. To do that, run the code cell below. If it worked correctly, you should get a return code of 0, and you should see the generated .html file in the workspace directory (click on the orange Jupyter icon in the upper left).
# 
# > Alternatively, you can download this report as .html via the **File** > **Download as** submenu, and then manually upload it into the workspace directory by clicking on the orange Jupyter icon in the upper left, then using the Upload button.
# 
# > Once you've done this, you can submit your project by clicking on the "Submit Project" button in the lower right here. This will create and submit a zip file with this .ipynb doc and the .html or .pdf version you created. Congratulations!

# In[70]:


from subprocess import call
call(['python', '-m', 'nbconvert', 'Analyze_ab_test_results_notebook.ipynb'])


# In[ ]:




