# Data wrangling project, WeRateDogs (@dog_rates) from twitter
# Project start date 21/12/2020 7:40 AM
# Primary code testing in pycharm, code transfer to Jupyter after functioning properly

# Import block
import pandas as pd
import numpy as np
import requests
import tweepy
import json

# Twitter API information block
api_key = 'cnM6fgsLgVbbUNf0dQ5NejsYU'
api_secret = 'KFDbzRIJdUQnlkjgcIYACWNiAli3YoZTUKdAbYDOUxHZi2m1WE'
token = '892121055283826691-w0toax2vedzi92Bn58QNk6rgx9Pu25M'
token_secret = 'QJjB71F5dQ3USMxGetALASV3pziNM2183BUpAwWQfkJbr'

# Location variables for files held on the home system
csv_loc = 'I:\\python\\pycharmprojects\\udacityproject1\\csv from classes\\'
json_loc = 'I:\\python\\pycharmprojects\\udacityproject1\\JSON\\'

# Import first file and analyse its contents
df1 = pd.read_csv((csv_loc + 'twitter-archive-enhanced.csv'))
i1 = df1.info()
s1 = df1.shape
u1 = df1.nunique()
d1 = sum(df1.duplicated())

print(i1,'\n', s1,'\n', u1,'\n', d1)

# Twitter search and download block
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(token, token_secret)
api=tweepy.API(auth, wait_on_rate_limit = True)

'''
with open('I:\\tweet_json.txt', 'w', encoding = 'utf8') as file:
    for tweet_id in df1.tweet_id:
        try:
            temp = api.get_status(tweet_id, tweet_mode = 'extended')
            json.dump(temp._json, file)
            file.write('\n')
        except:
            continue
'''

with open('tweet_json.txt', 'w') as outfile:
    # This loop will likely take 20-30 minutes to run because of Twitter's rate limit
    for tweet_id in tweet_ids:
        count += 1
        print(str(count) + ": " + str(tweet_id))
        try:
            tweet = api.get_status(tweet_id, tweet_mode='extended')
            print("Success")
            json.dump(tweet._json, outfile)
            outfile.write('\n')
        except tweepy.TweepError as e:
            print("Fail")
            fails_dict[tweet_id] = e
            pass
end = timer()
print(end - start)
print(fails_dict)

