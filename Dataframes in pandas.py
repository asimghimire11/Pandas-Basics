import pandas as pd
#Creating dataframe using List
# myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# df1 = pd.DataFrame(myList)
# print(df1)
#
# #Creating dataframe using Dictionary
# empData = {'empId' : [1, 2, 3, 4, 5], 'empName' : ["Asim", "Ashim", "Asheem", "Assem", "Asiim"]}
# df2 = pd.DataFrame(empData)
# print(df2)
#
# #Creating dataframe using Clipboard
# df3 = pd.read_clipboard()
# print(df3)

#Creating dataframe using excel file
df4 = pd.read_excel("C://Users/Victus/Documents/Excel/test.xlsx")
print(df4)

#Creating dataframe using csv file
df5 = pd.read_csv("C://Users/Victus/Documents/Excel/SS2016.csv")
print(df5)