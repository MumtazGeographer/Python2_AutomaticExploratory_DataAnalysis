import pandas as pd
import numpy as np

data = pd.Series(np.random.uniform(size=9), index=[['a','a','a','b','b','c','c','d','d'],
                                                   [1,2,3,1,3,1,2,2,3]])
print "Print Data \n",data

print "Index List \n", data.index

print "Only the index B \n", data['b']

print "Btw B & C index \n", data['b':'c']

print "LOC Function \n", data.loc[:,2]

print "Reshaping index with Unstack \n ", data.unstack()

frame = pd.DataFrame( np.arange(12).reshape((4, 3)),
                      index=[["a", "a", "b", "b"], [1, 2, 1, 2]],
                      columns=[["Ohio", "Ohio", "Colorado"], ["Green", "Red", "Green"]])

print "Print Frame data Here \n", frame

