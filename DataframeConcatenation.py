import pandas as pd

df1 = pd.DataFrame({'empname':['Asim', 'Ashim', 'Asheem', 'Aseem'], 'empsalary(in lakhs)':[30,29,31,40]})
df2 = pd.DataFrame({'empname':['Asim', 'Ashim', 'Asheem', 'Aaseem'], 'cdept':['CS', 'HR', 'CS', 'HR']})
df3 = pd.concat([df1,df2],ignore_index=True,axis=0)
print(df3)