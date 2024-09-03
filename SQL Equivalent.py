import pandas as pd
df = pd.read_excel("C://Users/Victus/Documents/Excel/student.xlsx")
# print(df)
#select * from student where Age in (17, 18)
# print(df[df.Age.isin([17,18])])
# print(df[df.Height.isin([144,180])])

#select * from student where Age not in (17, 18)
# print(df[~df.Age.isin([17,18])])
print(df[(df.Height.isin([144,180])) & (df.Weight >100)])
print(df[(~df.Height.isin([144,180])) & (df.Weight >100)])

