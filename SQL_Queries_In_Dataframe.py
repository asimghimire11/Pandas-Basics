import pandas as pd
df = pd.read_excel("C://Users/Victus/Documents/Excel/student.xlsx")
#select * from student
# print(df)
#select * from student where Age = 15
# print(df[df.Age == 15])
#select SN,Gender from student where Age = 15
# print(df[df.Age == 15][['SN','Gender']])
# print(df.columns)
#select SN, Gender, Weight from student where Weight<100
# print(df[df.Weight<100][['SN','Gender','Weight']])
print(df[df.Weight>100][['SN','Gender','Weight']])
