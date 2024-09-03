import numpy as np
import pandas as pd
import array as arr
sr = pd.Series()#empty series
myarr = arr.array('i', [10,20,30,40,50])
sr1 = pd.Series(myarr)#array series
print(sr1)

mylist = [100,200,300,400,500,600]
sr2 = pd.Series(mylist, index=['a','b','c','d','e','f'], name='my_series')
print(sr2)
print(sr2.name)
print(sr2.size)
print(sr2.ndim)#prints the dimension of the series
print(sr2.values)
print(sr2.shape)
print(sr2.nbytes)#print size of the values in series
print(sr2.memory_usage())#print the size of series including index and values
print(sr2.empty)#determines whether the series is empty or not