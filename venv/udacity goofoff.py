import pandas as pd

df_ans = pd.read_excel(r'I:\python\pycharmprojects\udacityproject1\anscombes-quartet.xlsx', engine='openpyxl')
print(df_ans.describe())

