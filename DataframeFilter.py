import pandas as pd
df = pd.read_excel("C://Users/Victus/Documents/Excel/student.xlsx")
print(df.columns)
# print(df.loc[(df['Gender'] == 'Female') & (df['Age'] >16)])
print(df.loc[(df['Gender'] == 'Male') & (df['Weight'] >100)])


