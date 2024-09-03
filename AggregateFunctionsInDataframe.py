import pandas as pd
# df = pd.read_excel("C://Users/Victus/Documents/Excel/student.xlsx")
# df1=df.groupby('Gender')
# for name,rows in df1:
#     print(name)
#     print(rows)
product = [('Limca', 25, 'BK'),('Limca', 40, 'NM'),('Frooti', 20, 'AK'),('Bmilk', 20, 'Amul'),('Bmilk', 20, 'Amul'),('Bmilk', 20, 'Sachi'),
('Limca', 15, 'AK'),('Frooti', 17, 'BK'),('Limca', 25, 'BK'),('Bmilk', 23, 'Sachi'),('Milk', 27, 'NK'),('Frooti', 23, 'BK')]

df=pd.DataFrame(product, columns=['Name', 'Price', 'Distributor'])
# print(df)
df1 = df.groupby('Name')
# for name, rows in df1:
#     print(name)
#     print(rows)

print(df1['Price'].agg(['max','min','mean','count','sum']))