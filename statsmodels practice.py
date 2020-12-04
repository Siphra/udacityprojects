import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

df = pd.read_csv(r'I:\Python\PycharmProjects\udacityproject1\csv from classes\house_price_area_only.csv')
df['intercept'] = 1

lm = sm.OLS(df.price, df[['intercept', 'area']])
results = lm.fit()
print(results.summary())