import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sb
import math
from patsy import dmatrices
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score, accuracy_score, confusion_matrix

# lesson 15 multiple linear regression question 4 has a mistake in its grading

df = pd.read_csv(r'I:\Python\PycharmProjects\udacityproject1\csv from classes\house_prices.csv')
df['intercept'] = 1
dfs = pd.get_dummies(df['style'])
dfn = pd.get_dummies(df['neighborhood'])

df_new = df.join(dfn)
df_new = df_new.join(dfs)


lm = sm.OLS(df_new.price, df_new[['intercept','bathrooms','bedrooms','area']])            #simple linear model
results = lm.fit()


y, X = dmatrices(' price ~ area + bedrooms + bathrooms', df, return_type='dataframe')
vif = pd.DataFrame()
vif["VIF Factor"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
vif["features"]=X.columns


df['bedrooms_squared'] = df.bedrooms * df.bedrooms
lm = sm.OLS(df.price, df[['intercept','bedrooms','bedrooms_squared']])            #simple linear model
results = lm.fit()

# Below is logistic regression testing above is for linear regression

df = pd.read_csv(r'I:\Python\PycharmProjects\udacityproject1\csv from classes\fraud_dataset.csv')
df[['weekday','weekend']] = pd.get_dummies(df.day)
df[['no-fraud','fraud']] = pd.get_dummies(df.fraud)
df['intercept'] = 1
lm = sm.Logit(df['fraud'],df[['intercept','duration']])
results = lm.fit()


lm = sm.Logit(df['fraud'],df[['intercept','weekday','duration']])
results = lm.fit()

df = pd.read_csv(r'I:\Python\PycharmProjects\udacityproject1\csv from classes\admissions.csv')
df[['1','2','3','4']] = pd.get_dummies(df.prestige)
df['intercept'] = 1
df.drop(['1'], axis=1, inplace=True)
log_mod = sm.Logit(df.admit, df[['intercept','gre','gpa','2','3','4']])
results = log_mod.fit()
gre_eb = math.exp(.0022)
gpa_eb = math.exp(.7793)
pre_eb = math.exp(-1.3387)
gpa_ebi = 1/gpa_eb
pre_ebi = 1/pre_eb

y= df['admit']

