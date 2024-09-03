import pandas as pd
df = pd.read_excel("C://Users/Victus/Documents/Excel/student.xlsx")
# print(df)
# print(df.loc[1:5, 'Gender'])
# print(".................................")
# print(df.loc[4])
print(df.iloc[1:4,[1,5]])
print(df.iloc[1:5,[1,2,3]])
print(df.iloc[:,[1,2,3,4]])