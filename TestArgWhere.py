import numpy as np
#prepare array lenght 6 of 2 rows and 3 files
x = np.arange(6).reshape(2,3)
print("Full array x: ")
print(x)
#find index for array element that satisfy given conditions
print("For condition >1, indexes are : ")
print(np.argwhere(x>1))
print("For condition >2, indexes are : ")
print(np.argwhere(x>2))
print("For condition ==1,indexes are : ")
print(np.argwhere(x==1))
