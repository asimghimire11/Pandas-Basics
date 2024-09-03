import pandas as pd
student = pd.read_excel("C://Users/Victus/Documents/Excel/student.xlsx")
# print(student)
# print(student.nlargest(5,'Height'))
print(student.nlargest(5,'Height').tail(3))
print(student.nlargest(5,'Height').head(3))