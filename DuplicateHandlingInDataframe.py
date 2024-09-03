import pandas as pd

df = pd.read_excel("C://Users/Victus/Documents/Excel/test.xlsx")
print(df.duplicated())

#if we want to reflect the changes in same dataframe we do as follows
df.drop_duplicates(inplace = True)
print(df.duplicated())
print(df)
df.to_excel("C://Users/Victus/Documents/Excel/newdata.xlsx",index=False)
print("Success")
#if we want to create new dataframe and store the data after removing duplicate values we do as follows
# df1=df.drop_duplicates()
# print(df1.duplicated())
# print(df1)