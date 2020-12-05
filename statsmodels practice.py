import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
# lesson 15 multiple linear regression question 4 has a mistake in its grading

df = pd.read_csv(r'I:\Python\PycharmProjects\udacityproject1\csv from classes\house_prices.csv')
df['intercept'] = 1
dfs = pd.get_dummies(df['style'])
dfn = pd.get_dummies(df['neighborhood'])

df_new = df.join(dfn)
df_new = df_new.join(dfs)


lm = sm.OLS(df_new.price, df_new[['intercept','bathrooms','bedrooms','lodge','victorian','B','C']])            #simple linear model
results = lm.fit()
print(results.summary())