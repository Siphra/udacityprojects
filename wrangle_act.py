#!/usr/bin/env python
# coding: utf-8

# # wrangle_act notebook
# ### analyze @dog_rates twitter 

# **Module Block**

# In[1]:


import pandas as pd
import numpy as np
import requests
import tweepy
import json
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import statsmodels.api as sm
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Gather

# In[2]:


# pulling in the image predictions:

url = 'https://d17h27t6h515a5.cloudfront.net/topher/2017/August/599fd2ad_image-predictions/image-predictions.tsv'
response = requests.get(url)
with open("image-predictions.tsv", mode = 'wb') as file:
    file.write(response.content)


# **This is a markdown cell but the below is the actual code used to download the file**
# 
# * api_key = 'Garbage to fill space'
# * api_secret = 'No I am your father'
# * token = 'So it\' s treason then?'
# * toen_secret = 'my precious'
# 
# * auth = tweepy.OAuthHandler(api_key, api_secret)
# * auth.set_access_token(token, token_secret)
# * api=tweepy.API(auth, wait_on_rate_limit = True)
# 
# 
# * with open('I:\\tweet_json.txt', 'a+', encoding = 'utf8') as file:
#   **   for tweet_id in df1.tweet_id:
#     ***    try:
#      ****       temp = api.get_status(tweet_id)
#       *****      json.dump(temp._json, file)
#        *****     file.write('\n')
#         **** except:
#           *****  continue

# ## Assess

# **Import first file, and analyze its contents.**

# In[3]:


df1 = pd.read_csv('twitter-archive-enhanced.csv')
df1


# In[4]:


df1.shape


# In[5]:


df1.info()


# In[6]:


df1.describe()


# In[ ]:





# In[7]:


sum(df1.duplicated())


# ### Issues in first file
# 
# #### Quality
# * Large number of NaN's in multiple columns 
#     * ['in_reply_to_status_id', 
#     * 'in_reply_to_user_id', 
#     * expanded_urls
# * timestamps are not in datetime data type
# * duplicate dog names may or may not be same dog
# * Mislabled data types for four categoricals 'doggo', etc
# * No data for categorical options doggo, floofer, pupper, puppo
# * Maximum rating for a dog is 1776, unless this is george washington's dog, probably incorrect
# * Denominators should all be 10, we have at least one larger than that
# 
# Note that some other columns had a large number of NaNs but were going to be dropped for final analysis anyway.
# 
# #### Tidiness
# 
# * 4 categories should be a single column, 'doggo' etc.
# 
# 
# 

# **Second file 'Image Predictions TSV file' block**

# In[8]:


df2 = pd.read_csv('image-predictions.tsv', sep='\t')
df2


# In[9]:


df2[df2['p1_conf'] == 1]


# In[10]:


df2.info()


# In[11]:


df2.nunique()


# In[12]:


df2.describe()


# ### Issues in second file
# 
# * Each row is not an observational unit, p1-p3 should be combined into a single column, and assigned a category variable
# * One unit has p1_conf of 1.0 we need to validate that p2 & p3 are both 0
# * tweet_id should be str not int
# * img_num should be str not int

# ### analyzing the third file

# In[13]:


df3 = pd.DataFrame(columns = ['tweet_id', 'retweet_count', 'favorite_count'])
with open ('tweet_json.txt') as file:
    for line in file:
        tweet = json.loads(line)
        t_id = tweet['id_str']
        r_ct = tweet['retweet_count']
        f_ct = tweet['favorite_count']
        df3 = df3.append(pd.DataFrame([[t_id,r_ct,f_ct]],columns = ['tweet_id', 'retweet_count', 'favorite_count']))
df3.reset_index(drop = True, inplace = True)
df3.head()


# In[14]:


df3.info()


# In[15]:


df3.shape


# In[16]:


type(df3.retweet_count[0])


# ## Clean

# In[17]:


# create copies for cleaning process

df1_c = df1.copy()
df2_c = df2.copy()
df3_c = df3.copy()


# * Find and locate items that are retweets of original tweet. Remove these rows. 
#     * First change all NaN's in retweet_status to zeros
#     * Locate all positions where the status is not zero
#     * Remove those rows
#     * Drop retweeted status column

# In[18]:


# Since we're replacing NaN's in one column we might as well do this is all columns for df1

df1_c = df1_c.fillna(0)
df1_c.retweeted_status_id = df1_c.retweeted_status_id.astype('int')
df1_p = df1_c[df1_c['retweeted_status_id'] != 0] #create purge dataframe
df1_c = df1_c.drop(df1_p.index)
df1_c.drop(columns=['retweeted_status_id','retweeted_status_user_id', 'retweeted_status_timestamp'], inplace = True)

df1_c.head()


# In[19]:


# After identifying bad names in the name column, I've decided to fix that in this block where we fix NaNs
df1_c['name'].replace({'a':'None', 'an':'None', 'the':'None'}, inplace=True)
df1_c.name.value_counts()


# * Change timestamp column to datetime datatype.

# In[20]:


df1_c.timestamp = pd.to_datetime(df1_c.timestamp)
df1_c.info()


# * Convert columns in df1 to correct datatypes 

# In[21]:


#while I could have grouped these operations, in the event one needed to be reversed it is easier to keep them
# as seperate operations.
df1_c.tweet_id = df1_c.tweet_id.astype(str)
df1_c.in_reply_to_status_id = df1_c.in_reply_to_status_id.astype(int)
df1_c.in_reply_to_user_id = df1_c.in_reply_to_user_id.astype(int)
df1_c.in_reply_to_status_id = df1_c.in_reply_to_status_id.astype(str)
df1_c.in_reply_to_user_id = df1_c.in_reply_to_user_id.astype(str)

#including df2 here as well

df2_c.tweet_id = df2_c.tweet_id.astype(str)
df2_c.img_num = df2_c.img_num.astype(str)

df1_c.info()


# * convert doggos, etc. to categories and merge into single column

# In[22]:


df1_c[['doggo','floofer','pupper','puppo']].apply(pd.Series.value_counts)


# In[23]:


df1_c[df1_c['floofer'] == 'floofer']


# In[24]:


df1_c[df1_c['pupper'] == 'pupper']


# In[25]:


df1_c[df1_c['puppo'] == 'puppo']


# In[26]:


pd.set_option("mode.chained_assignment", None) #suppress setting with copy warning. In general this is a bad idea.
# create new column and change its datatype
df1_c['dog_type'] = 'Null'
for i in df1_c.index:
    if df1_c.doggo[i] == 'doggo':
        df1_c['dog_type'][i] = 'doggo'
    elif df1_c.floofer[i] == 'floofer':
        df1_c['dog_type'][i] = 'floofer'
    elif df1_c.pupper[i] == 'pupper':
        df1_c['dog_type'][i] = 'pupper'
    elif df1_c.puppo[i] == 'puppo':
        df1_c['dog_type'][i] = 'puppo'
    else:
        df1_c['dog_type'][i] = 'None'
df1_c.dog_type = df1_c.dog_type.astype('category')
df1_c.info()


# In[27]:


pd.set_option("mode.chained_assignment", "warn") #restore warning about set with copy
#drop all unneeded rows from df1_c
df1_c.drop(['doggo', 'floofer', 'pupper', 'puppo'], axis = 1, inplace = True)
df1_c.head()


# In[28]:


df1_c.rating_denominator.value_counts()


# In[29]:


#normalizing all ratings and denominators to x/10
df1_c['rating_numerator_norm'] = 10 * df1_c.rating_numerator/df1_c.rating_denominator
df1_c['rating_denominator_norm'] = 10 * df1_c.rating_denominator/df1_c.rating_denominator
df1_c.info()


# In[30]:


# drop denominator 0 row
df1_c.drop(index = 313, inplace = True)
# swap denominators and numerators from float to int
df1_c.rating_denominator_norm = df1_c['rating_denominator_norm'].astype(int)
df1_c.rating_numerator_norm = df1_c['rating_numerator_norm'].astype(int)
# drop old non-normalized columns
df1_c.drop(columns=['rating_numerator','rating_denominator'], inplace=True)


# In[31]:


df1_c.rating_numerator_norm.describe(),df1_c.rating_denominator_norm.describe(),df1_c.info()


# In[32]:


df3_c.retweet_count = df3_c.retweet_count.astype(int)
df3_c.favorite_count = df3_c.favorite_count.astype(int)


# In[33]:


#verify all datatypes are correct
df1_c.info(), df2_c.info(),df3_c.info()


# In[34]:


# split df3_c into 2 dataframe named df3_c_r and df3_c_f
df3_c_r = df3_c.drop(columns='favorite_count')
df3_c_f = df3_c.drop(columns='retweet_count')
# split df1_c into 2 daframes named df1_c and df1_doggo
df1_doggo = df1_c[['tweet_id','dog_type']]
df1_c.drop(columns=['dog_type'], inplace = True)
df3_c_r.info(), df3_c_f.info(), df1_c.info(), df1_doggo.info()


# In[35]:


# get all datasets the same size for operations between them
#first determine which order provides the smallest dataset.
x = sum(df1_c.tweet_id.isin(df2_c.tweet_id))
y = sum(df1_c.tweet_id.isin(df3_c.tweet_id))
z = sum(df2_c.tweet_id.isin(df3_c.tweet_id))


# In[36]:


# first cut the new df1_c via df2, then via df3.
df1_c = df1_c[df1_c['tweet_id'].isin(df2_c['tweet_id'])]
df1_c = df1_c[df1_c['tweet_id'].isin(df3_c['tweet_id'])]
df2_c = df2_c[df2_c['tweet_id'].isin(df3_c['tweet_id'])]
df2_c = df2_c[df2_c['tweet_id'].isin(df1_c['tweet_id'])]
df3_c_r = df3_c_r[df3_c_r['tweet_id'].isin(df1_c['tweet_id'])]
df3_c_f = df3_c_f[df3_c_f['tweet_id'].isin(df1_c['tweet_id'])]


# In[37]:


# make sure all dataframes are the same size:
df1_c.shape,df2_c.shape,df3_c_r.shape,df3_c_f.shape


# In[38]:


#make sure the datat they contain all has the same tweet ids
df1_c.tweet_id.isin(df2_c.tweet_id).value_counts(),df1_c.tweet_id.isin(df3_c_f.tweet_id).value_counts()


# In[39]:


df1_c.to_csv('twitter_archive_master.csv', encoding='utf-8')
df1_doggo.to_csv('twitter_archive_doggo.csv', encoding='utf-8')
df2_c.to_csv('image_predictions_master.csv', encoding='utf-8')
df3_c_r.to_csv('recount_master.csv', encoding='utf-8')
df3_c_f.to_csv('favorite_master.csv', encoding='utf-8')


# ## Analyze

# ### Impact of time on retweet numbers

# In[56]:


# Analysis for tweet time impact on retweet numbers

dfa1 = df1_c.merge(df3_c_r, how = 'left', on = 'tweet_id')
dfa1.head()


# In[41]:


times = dfa1.timestamp.dt.strftime('%H:%M')
x = np.arange(len(times))
plt.figure(figsize = (20,8))
plt.plot(x, dfa1.retweet_count, 'o')
plt.xlabel('time in 24hr format')
plt.ylabel('retweets')
plt.show()


# ### Impact of having a name on retweet numbers

# In[53]:


# Check if having a name has an impact create dataframe dfa2
pd.set_option("mode.chained_assignment", None)
dfa2 = df1_c[['tweet_id','name']].merge(df3_c_r, how = 'left', on = 'tweet_id')
# We're not intersted in seeing if a specific name is better, but rather if names in general are
# in order to facilitate this, we're going to shift ALL names to 1, and all "None" to 0 
dfa2.name = dfa2.name.apply(lambda dfa2 : 0 if dfa2 == 'None' else 1)
dfa2.tail()


# In[43]:


#difference in means for analysis
dfa2_dm = dfa2[dfa2.name == 1].retweet_count.mean() - dfa2[dfa2.name == 0].retweet_count.mean() 


# In[44]:


# Analysisto determine if the difference in retweet counts is significant or not.
named, notnamed, diffs = [] , [], []
for _ in range(10000):
    bootsamp = dfa2.sample(dfa2.shape[0], replace = True)
    noname_mean = bootsamp[bootsamp['name'] == 0]['retweet_count'].mean()
    name_mean = bootsamp[bootsamp['name'] == 1]['retweet_count'].mean()
    # append the info 
    notnamed.append(noname_mean)
    named.append(name_mean)
    diffs.append(name_mean - noname_mean)   
#split the two dataframes up to allow for independent random samples


# In[45]:


#generate stds
std_name = np.std(named)
std_noname = np.std(notnamed)
std_dif = np.std(diffs)

std_name, std_noname, std_dif


# In[46]:


#historgam plot of the variable 'name' for named (blue) and unnamed dogs (orange)
plt.hist(named, alpha = .5)
plt.hist(notnamed, alpha = .5)
plt.xlabel('retweet counts')


# In[47]:


#generate a null sample based on the differences in tweets
null_vals = np.random.normal(0, np.std(diffs), 10000)


# In[48]:


# histogram for the null and actual variation means.
plt.hist(diffs, alpha = .5)
plt.hist(null_vals, alpha = .5)
plt.axvline(dfa2_dm, color='red')
plt.xlabel('retweet count differences')


# In[59]:


#calculate the p_value for if our mean is > .05
p_dfa2 = (null_vals > dfa2_dm).mean()
p_dfa2


# ### Impact of dog 'type' on retweet numbers

# In[50]:


#checking the impact of dog type on retweet counts create dfa3 dataframe
dfa3 = df1_doggo.merge(df3_c_r,how = 'left', on = 'tweet_id')
dfa3.head()


# In[51]:


dfa3[['None', 'doggo', 'floofer', 'pupper', 'puppo']] = pd.get_dummies(dfa3.dog_type)
dfa3.head()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




