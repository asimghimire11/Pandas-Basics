import pandas as pd

df = pd.read_excel("C://Users/Victus/Documents/Excel/test.xlsx")
#print(df.sort_index(ascending=False))
print((df.sort_values('City Name')))