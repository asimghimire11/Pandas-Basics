import pandas as pd
df1 = pd.DataFrame({'empid':[1,2,3,4],'empname':['Asim', 'Ashim', 'Asheem', 'Aseem']})
df2 = pd.DataFrame({'empid':[1,2,3,5],'empdept':['CS', 'HR', 'CS', 'HR']})
# print("Dataframe 1: ")
# print(df1)
# print(pd.merge(df1,df2, on='empid', how='inner')) #inner join
# print(pd.merge(df1,df2, on='empid', how='outer')) #outer join
# print(pd.merge(df1,df2, on='empid', how='left')) #left join
# print(pd.merge(df1,df2, on='empid', how='right')) #right join

#When there is no common column in both dataframes
df3 = pd.DataFrame({'empname':['Asim', 'Ashim', 'Asheem', 'Aseem'], 'empsalary(in lakhs)':[1,2,3,4]})
df4 = pd.DataFrame({'citizen':['Asim', 'Ashim', 'Asheem', 'Aaseem'], 'cdept':['CS', 'HR', 'CS', 'HR']})

print(df3)
print(df4)

print(pd.merge(df3, df4, left_on='empname', right_on='citizen', how='inner'))
print(pd.merge(df3, df4, left_on='empname', right_on='citizen', how='left'))
print(pd.merge(df3, df4, left_on='empname', right_on='citizen', how='right'))
print(pd.merge(df3, df4, left_on='empname', right_on='citizen', how='outer'))
