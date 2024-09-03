import pandas as pd
product = [('Limca', 25, 'BK'),('Limca', 40, 'NM'),('Frooti', 20, 'AK'),('Bmilk', 20, 'Amul'),('Bmilk', 20, 'Amul'),('Bmilk', 20, 'Sachi'),
('Limca', 15, 'AK'),('Frooti', 17, 'BK'),('Limca', 25, 'BK'),('Bmilk', 23, 'Sachi'),('Milk', 27, 'NK'),('Frooti', 23, 'BK')]

df=pd.DataFrame(product, columns=['Product_Name', 'Product_Price', 'Distributor'])
# print(df)
df1 = df.groupby('Product_Name')
# for name,rows in df1:
#     print(name)
#     print(rows)
# print(df1.get_group('Bmilk'))
# print(df1.get_group('Limca').max())
print(df1.max())