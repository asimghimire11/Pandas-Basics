import pandas as pd
df = pd.read_excel("C://Users/Victus/Documents/Excel/student.xlsx")
#Insert data into dataframe
# df1=df._append({'SN':217,'Gender':'Female',	'Age':18,'Address':'T','Height':180,'Weight':100,'Eye':'Black','Medu':5,'Fedu':8,'Fsize':'Ab5'},ignore_index=True)
# print(df1)
#Update the data of the certain column in dataframe
# df.loc[df['Eye']=='Blue','Eye']='Black'
print(df)
print(".....................After Update..................")
df = df.drop(df[df.Age==17].index)
print(df)