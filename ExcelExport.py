import pandas as pd

df = pd.read_excel("C://Users/Victus/Documents/Excel/test.xlsx")

df['2015_Score'] = df['2016_Score'] + df['2017_Score']
print(df)

df.to_excel("C://Users/Victus/Documents/Excel/test.xlsx",index=False)
print("Success")