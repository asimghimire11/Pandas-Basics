import pandas as pd
df = pd.read_excel("C://Users/Victus/Documents/Excel/test.xlsx")
df.set_index('City Name', inplace=True)
# print(df.where(df<2000,'First'))
# print(df.where(df['2016_Score']<1500,'First'))

print(df.where(lambda x:x<1800, 'First'))
