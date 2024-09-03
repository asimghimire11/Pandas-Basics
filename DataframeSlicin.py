import pandas as pd
df = pd.read_excel("C://Users/Victus/Documents/Excel/newdata.xlsx")
# print(df.head(3)) #Print top 3 rows
# print(df.tail()) #Print bottom 5 rows
# print(df.columns) #Print all columns name
# print(df['City Name']) #Prints all the rows of City Name column
# print(df[['City Name', '2018_Score']]) #Print all the values of two columns
# print(df[1:19]) #Prints the records of only specified rows
# print(df[1:19:3]) #here 3 is increment (works similarly as for loop) [start:stop:increment]
print(df[['City Name', '2018_Score']][1:19:3]) #prints the data of specified columns and rows



