# CLA in python
# =============
# Python supports CLA which stands for  command line argument.CLA or command line argument can be represent as if we are passing one or more than one
# one arguments at time of execution of the python script then it is said to be
# CLA or command line argument.In python we do have a predefine module named as
# sys module.Inside the sys module we do have a variable named as argv variable


# ->argv returns the data or information in List format
# ->While working with argv variable each object is in stirng type
# ->indexing is applicable for argv variable
# ->slicing is applicable for argv variable
# ->While working with argv variable each object inside the list string type as
# the applicaiton reqn we need to perform typecasting.
# ->If you want to read full_name we must use "" not '' 


# Ex1:
# ====
# import time 

# import time 
# from sys import * 
# print(argv)
# print()
# print(type(argv))
# print()
# time.sleep(2)
# print('End of an application')

# from sys import*
# print(argv)
# print()
# print(type(argv))

# Ex2:
# ====
# import time 
# from sys import * 
# print(argv)
# print()
# print(type(argv))
# print()
# print("====Indexing====")
# print(argv[0])
# print(argv[1])
# print(argv[2])
# print(argv[3])
# print(argv[4])
# print()
# time.sleep(2)
# print('End of an application')


# from sys import *
# print(argv)
# print(type(argv)) 


# Ex3:
# ===
# import time 
# import sys
# print(argv)
# print()
# print(type(argv))
# print()
# print("====Slicing====")
# print(argv[1:])
# print()
# time.sleep(2)
# print('End of an application')

# import time 
# from sys import * 
# print(argv)
# print()
# print(type(argv))
# print()
# print("====Slicing====")
# print(argv[1:])
# print()
# time.sleep(2)
# print('End of an application')

# # from sys import 

# def fn(*a):
#     print(a)
# fn(1,2,2,3,4,5,6,7)

# from sys import *
# print(argv)
# print()
# print(type(argv))
# print()
# print(argv[2:])
# print()

# from sys import*
# print(argv)
# print()
# print(argv[0])
# print(argv[2])
# print(argv[4])
# print(argv[5])
# print(argv)
# print(argv[1:])
# print()
# print(argv[3:])
# print()
# print(argv[5:])
# print(argv)

# from sys import*
# print(argv)
# print()
# print(argv[0])
# print(argv[2])
# print(argv[4])
# print(argv[5])
# print(argv)
# print(argv[1:5])
# print()
# print(argv[3:6])
# print()
# print(argv[5:7])
# print(argv)


# Ex4:
# ====
# import time 
# from sys import * 
# print(argv)
# print()
# print(type(argv))
# print()
# print("==== + ====")
# print(argv[1]+argv[2]+argv[3]+argv[4])
# print()
# time.sleep(2)
# print('End of an application')

# from sys import*
# print(argv)
# print()
# print(type(argv))
# print()
# print(argv[1]+argv[2]+argv[3])
# print()

# from sys import*
# print(argv)
# print(type(argv))
# print()
# print(int(argv[1]+argv[2]+argv[3]+argv[4]))
# print()



# Ex6:
# ====
# import time 
# from sys import * 
# print(argv)
# print()
# print(type(argv))
# print()
# print("==== + ====")
# print(int(argv[1])+int(argv[2])+int(argv[3])+int(argv[4]))
# print()
# time.sleep(2)
# print('End of an application')

# from sys import*
# print()
# print(type(argv))
# print(argv)
# print()
# print(int(argv[1])+int(argv[2])+int(argv[3])+int(argv[4])+int(argv[5]))
# print()

# import time 
# from sys import * 
# print(argv)
# print()
# print(type(argv))
# print()
# S1=0
# for x1 in argv[1:]:
#     x2=int(x1)
#     S1=S1+x2
# print("Sum of any number of arguments:",S1)
# print()
# time.sleep(2)
# print("End of an application")


# from sys import*
# print()
# print(argv)
# print()
# print(type(argv))
# print()
# s1=0
# for lite in argv[1:]:
#     lite2=int(lite)
#     s1=s1+lite2
# print("sum of any number of arguments:",s1)
# print()


# from sys import*
# print()
# print(argv)
# print(type(argv))
# print()
# m1=0
# for s1 in argv[1:]:
#     s2=int(s1)
#     s1=s1+m1
# print(s1)


# from sys import*
# print()
# print(argv)
# print(type(argv))
# y1=0
# for m1 in range[1:]:
#     m2=int(m1)
#     m1=m1+y1
# print(m1)

# from sys import *
# print()
# print(argv)
# print(type(argv))
# t1=0
# for s1 in argv[1:]:
#     s2=int(s1)
#     t1=t1+s2
# print()
# print(t1)

# from sys import*
# a=eval(input("enter the values:"))
# c=[]
# d=[]
# for b in a:
#     if(b%2==0):
#         #print(b)
#         c.append(b)
#     else:
#         d.append(b)
# print(f"even number's are {c}")
# print(f"even number's are {d}")

# from sys import*
# a=eval(input("enter the value:"))
# b=[]
# for c in a:
#     if(c%2==0)
#     b.append(c)
# print("even values are:",b)
        


# import time 
# from sys import * 
# print(argv)
# print()
# print(type(argv))
# print()
# S1=0
# for x1 in argv[1:]:
#     x2=int(x1)
#     S1=S1+x2
# print("Sum of any number of arguments:",S1)
# print()
# time.sleep(2)
# print("End of an application")

# Ex9:
# ==== 
# import time 
# from sys import * 
# print("My full_name is:",argv[1])
# print()
# time.sleep(2)
# print('End of an application')

from sys import*
S1=0
for x1 in argv[1:]:
    x2=int(x1)
    S1=S1+x2
print(S1)
  


# def add(a,b):
#     print(a+b)
# add(10,20)


# from sys import*
# print(argv)
# print()
# print(type(argv))
# s=0
# for x1 in argv[:1]:
#     y=int(x1)
#     b=y+
# print(b)
# print()
    

# import time 
# from sys import * 
# print(argv)
# print()
# print(type(argv))
# print()
# S1=0
# for x1 in argv[1:]:
#     x2=int(x1)
#     S1=S1+x2
# print("Sum of any number of arguments:",S1)
# print()
# time.sleep(2)
# print("End of an application")
