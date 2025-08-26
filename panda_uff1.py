# import pandas as pd
# data=[[1001,"mobile",18800,"oppo"][1002,"mobile",21000,"redmi"][1003,"mobile3",180000,"apple"][1004,"mobile4",250000,"techno"]]
# obj1=pd.DataFrame(data,columns=["pid","pname","price","company"],index=["l1","l2","l3","l4"])
# print("============================================")
# print(obj1)
# print("==============================================")
# print()
# print()
# print("---sum---")
# print(obj1.sum())
# print()

# import pandas as pd
# data=[[1001,"mobile",18000,"oppo"],[1002,"mobile2",21000,"redmi"],[1003,"mobile3",23000,"lenovo"]]
# obj1=pd.DataFrame(data,columns=["pid","pname","price","company"],index=["l1","l2","l3"])
# print("==================================================")
# print()
# print(obj1)
# print("==================================================")
# print()

# import pandas as pd
# print(dir(pd))
  
# import pandas as pd
# import numpy             # .ndim is used to show the dimensions....
# s1=pd.DataFrame([1001,1002,1003,1004,1005,1006])
# print(s1)
# print(s1.ndim)
# print()


# import pandas as pd
# import numpy                  # only two dimensional values are given in columns and rows format...
# s1=pd.DataFrame([[1001,1002,1003,10004,10005],[2001,2002,2003,2004,2005]])
# print(s1)
# print()
# print(s1.ndim)

# import pandas as pd           #if full data is not available result will given ..."none"... on missing data.. 
# y=pd.DataFrame([[131,141,151,161],[1,25,1,45,15,45],[1,5,12,521,5,2,52,52,5,5]])
# print(y)
# print(y.ndim)
# print()

# import pandas as pd
# y=pd.DataFrame([[1001,1002,1003,1004,1005],[2001,2002,2003,2004]])
# print()
# print(y)
# print(y.ndim)

# import pandas as pd             # .ndim is used to show the dimensions....
# s1=pd.DataFrame([1001,1002,1003,1004,1005,1006])
# print(s1)
# print(s1.ndim)
# print()

# import pandas as pd
# like=[["car1","bottle1",111],["car2","bottle2",222],["car3","bottle2",333],["car4","bottle3",444]]
# m1=pd.DataFrame(like)
# print()
# print(m1)
# print()

# import pandas as pd   
# print()                      # invalid  syntax the output will be shown.../////////.../../.././
# like=pd.DataFrame([["car1","bottle1",111],["car2","bottle2",222],["car3","bottle2",333],["car4","bottle3",444],[columns=["iii","kkk","lll"]],[index=[1,2,3]]])
# print(like)
# print()

# import pandas as pd
# like=pd.DataFrame([["car1","bottle1",111],["car2","bottle2",222],["car3","bottle2",333]])
# print(like)
# print()

# import pandas as pd
# like=pd.DataFrame([["car1","bottle1",111],["car2","bottle2",222],["car3","bottle2",333],["car4","bottle3",444]])
# print(like)
# print()

"""#=========.........TO GIVE "COLUMNS" N "ROWS" names we have to take SEPARATE VARIABLE LIST........=======#"""

# import pandas as pd
# meteor=[[111,222,333,444],[555,666,777,888],[000,101,102,103]]
# sky=pd.DataFrame(meteor,columns=["DESIGN1","DESIGN2","DESIGN3","DESIGN4"],index=["path1","path2","path3"])
# print()
# print(sky)

'''@@@....##....in index we have to take how many data_sets we rae taking....... '''
"""###....in columns we have to take the objects in the data sets..........."""


# import time 
# import pandas as pd
# Products_Data_Sets=[[1001,"Mobile_1",23000,"S1"],[1002,"Mobile_2",24000,"S2"],[1003,"Mobile_3",25000,"S3"],[1004,"Mobile_4",26000,"S4"],[1005,"Mobile_2",27000,"S5"],[1006,"Mobile_6",28000,"S6"]]
# S1=pd.DataFrame(Products_Data_Sets,columns=['Pid','Pname','Price','Company'],index=['IHUB_1','IHUB_2','IHUB_3','IHUB_4','IHUB_5','IHUB_6'])
# print()
# print("=====Product_Details======")
# print(S1)
# print()
# print(S1.sum())
# time.sleep(2)
# print("End of an application")

# import pandas as pd
# product=[[1001,"mobile",21000,"iphone"],[1002,"mobile2",22000,"iphone2"],[1003,"mobile3",23000,"iphone3"],[1004,"mobile4",24000,"iphone4"]]
# s1=pd.DataFrame(product,columns=["pid","name","price","company"],index=["list1","list2","list3","list4"])
# print(s1)
# print()
# print(s1.sum())
# print()

# import pandas as pd
# meteor=[[111,222,333,444],[555,666,777,888],[000,101,102,103],[104,105,106,108]]
# sky=pd.DataFrame(meteor,columns=["DESIGN1","DESIGN2","DESIGN3","DESIGN4"],index=["path1","path2","path3","path4"])
# print()
# print(sky)
# print(sky.ndim)
# print(sky.head(2))
# print()
# print(sky.tail(2))
# print()
# print(sky.sum(1))     #....it EWILL CALCULATE ROWS VALUES.....
# print()
# print(sky.sum())      #.....IT WILL CALCULATE COLUMN VALUES.....
# print()
#  #print(sky.sum(2))     #...///.....IT will not allow another values above 1 to calculate columns or rows.....

# import pandas as pd
# meter=[[111,222,333,444],[555,666,777,888],[100,101,102,103],[104,105,106,108]]
# obj1=pd.DataFrame(meter)
# print("====================")
# print()
# print(obj1)
# # a=0
# # for b in obj1:
# #     a=a+b         ##..not applicable for pandas module
# # print()
# # print(a)
# # print(a.sum(1))


import pandas as pd
data_information=[[1001,"mobile1",27000,"sony"],[1002,"mobile_2",28000,"oppo"],[1003,"mobile_3",29000,"apple"],[1004,"mobile_4",30000,"pineapple"]]
obj1=pd.DataFrame(data_information,columns=["pid,","pname","price","company"],index=["path1","path2","path3","path4"])
print()
print(obj1)
print(obj1.sum(1))
print()
print(obj1.sum())
print()
print(obj1.max())
print()
print(obj1.min())
print()
print(obj1.head(2))
print()
print(obj1.tail(2))
print()


