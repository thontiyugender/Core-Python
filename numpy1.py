#  numpy module:
#=================

# it is a predefine module od library.numpy means numerical python.numpy represent the data or information in an array dimention format.
# numpy is more faster than list data type.dimentions can 0 to nth dimension.

# import numpy as np
# s1=np.array(1200)
# print("the value is:",s1)
# print()
# print("the dimentions are:",s1.ndim)
# print()


# import numpy as np
# s1=np.array([100,200,300,400,500])
# print("the value is:",s1)
# print()
# print("the dimentions are:",s1.ndim)
# print()

# import numpy as np
# s1=np.array([1000,2000,3000,4000,5000])
# print()
# print(s1.ndim)
# print()
# print("======using indexing=====")
# print()
# print(s1[0])
# print(s1[1])
# print(s1[2])
# print(s1[3])
# print()

# import  numpy as np
# s1=np.array([100,200,300,400,500,600])
# print("the dimentions are:",s1.ndim)
# print("====using slice operations====")
# print()
# print(s1[0:])
# print(s1[1:])
# print()
# print(s1[::-1]) ##...----->>reverse object
# print(s1[0:3])
# print(s1[-1:4:-1])

# import numpy as np
# s1=np.array([22,5,5,555,545,454544,54,5])
# print(s1.ndim)
# print(s1[1:])
# print(s1[2:])
# print(s1[4:])
# print()
# for x in (s1[4:]):
#     print(x)
# print()
# print()

import numpy as np
s1=np.array([1,2,3,4,5,6,7,8,9])
s2=np.array([1,2,3,4,5,6,7,8,9])
print(s1.ndim)
print(s2.ndim)
print()
print(s1+s2)
print()


# import numpy as np
# s1=np.array([[1000,2000,3000,4000,5000],[10,20,30,40,50]])
# print("the value is:",s1.ndim)
# print()
# print("the dimentions are:",s1.ndim)
# print()
# print("-----two dimensional array-----")
# print(s1[0][3])
# print()
# print(s1[1][3])
# print()

# import numpy as np
# s1=np.array([[[100,200,300,400,500],[1000,2000,3000,4000,5000]]])
# print("the value is:",s1)
# print()
# print("the dimentions are:",s1.ndim)
# print()

# import numpy as np
# s1=np.array([[[1,2,3,4,5],[3,5,6,2]]])
# print()
# print(s1)                                       ###...when value is cancel out the value is not deleted...
# print()
# d2=s1.shape
# print("the result is:",d2)
# print()
# print("the dimentions are:",s1.ndim)
# print()

# import numpy as np
# s1=np.array([[[1,2,3,4,5],[3,5,6,2,1]]])
# print()
# print(s1)
# print()
# d2=s1.shape
# print("the result is:",d2)
# print()
# print("the dimentions are:",s1.ndim)
# print()

# import numpy as np
# s1=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print()
# print(s1)
# d2=s1.reshape(6,2)
# print("the result is:",d2)
# print()
# print("the dimentions are:",s1.ndim)
# print()


# import numpy as np
# s1=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print()
# print(s1)
# print()
# d2=s1.reshape(4,3)
# print("the result is:",d2)
# print()
# print("the dimentions are:",s1.ndim)
# print()
# for x1 in d2:
#     for y1 in x1:
#         print(y1,end=" ")
#     print()
# print()

# import numpy as np
# s1=np.array([1,2,3,4,5,6,7,8,9,10,11,12],ndmin=9)
# print(s1)                                        ####....to give many dimensions we use ndmin...
# print()                                          ####....to count how many presents are there.....
# print(s1.ndim)
# print()

# import numpy as np
# s1=np.array(["A","A","A","A","A","A","A","A","A","A","A","A"])
# print(s1)
# print()
# d2=s1.reshape(3,3)
# print()
# print("the dimentions are:",d2.ndim)
# print()                                      ##...failure...
# for y1 in d2:
#     for z1 in y1:
#         print(z1,end=" ")
#     print()
# print()



