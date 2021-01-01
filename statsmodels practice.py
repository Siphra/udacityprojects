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
df[['1', '2', '3', '4']] = pd.get_dummies(df.prestige)
df['intercept'] = 1
#df.drop(['1'], axis=1, inplace=True)
log_mod = sm.Logit(df.admit, df[['intercept', 'gre', 'gpa', '2', '3', '4']])
results = log_mod.fit()
gre_eb = math.exp(.0022)
gpa_eb = math.exp(.7793)
pre_eb = math.exp(-1.3387)
gpa_ebi = 1/gpa_eb
pre_ebi = 1/pre_eb

y = df['admit']
X = df[['gre', 'gpa', '1', '2', '3']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10, random_state=42)
log_mod = LogisticRegression()
log_mod.fit(X_train, y_train)
y_pred = log_mod.predict(X_test)
print(df.head())
print(precision_score(y_test, y_pred))
print(recall_score(y_test, y_pred))
print(accuracy_score(y_test ,y_pred))
print(confusion_matrix(y_test, y_pred))

#below is project code

df = pd.read_csv(r'I:\Python\PycharmProjects\udacityproject1\csv from classes\ab_data.csv')
print(df.head())
print(df.info())
print(df.nunique())
print(sum(df.converted)/df.user_id.nunique())
dfchk = df[df['group'] == 'treatment']
dfchkop = df[df['group'] == 'control']
dfchk = dfchk[dfchk['landing_page']== 'old_page']
dfchkop = dfchkop[dfchkop['landing_page'] == 'new_page']
dfchk = dfchk.append(dfchkop)
print(dfchk.info())
df2 = df[~df.isin(dfchk)].dropna()
print(df2.head())
print(df2[((df2['group'] == 'treatment') == (df2['landing_page'] == 'new_page')) == False].shape[0])
print(df2.nunique())
dups = df2[df2.user_id.duplicated(keep = False)==True]
print(dups)
df2.drop(2893, axis=0, inplace=True)
print(df2.shape)
conv = sum(df2.converted)/df2.shape[0]
print(conv)
dfc = df2[df2.group == 'control']
print(sum(dfc.converted)/dfc.shape[0])
dft = df2[df2.group == 'treatment']
print(sum(dft.converted)/dft.shape[0])
print(sum(df2.group == 'treatment')/df2.shape[0])
print(conv,conv, dft.shape[0], dfc.shape[0])

new_page_converted = np.random.choice([0,1], dft.shape[0],replace= True, p=[conv,1-conv])
old_page_converted = np.random.choice([0,1], dfc.shape[0], replace= True, p=[conv, 1-conv])
plt.hist(new_page_converted, color='green')
plt.hist(old_page_converted, color='red')
plt.show()

