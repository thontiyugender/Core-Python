
# ->Uniary operator:
# ==================
# # Uniary operator can be represent if we are using one operator with one variable then it is said to be Uniary operator.

# Ex1:
# ===
# import time
# X1=True 
# print(X1)
# print()
# print(type(X1))
# print()
# X2=not X1
# print(X2)
# print()
# print(type(X2))
# print()
# time.sleep(2)
# print('End of an application')


# x1=False
# print()
# print(x1)
# print(type(x1))
# X2=not x1
# print(X2)
# print(type(X2))

# x1=True
# print()
# print(x1)
# print(type(x1))
# x2=not x1
# print(x2)
# print(type(x2))

# ->Binary operator:
# ==================
# Binary operator can be represent as if we are using two operand or two variables with one operator then it is said to be Binary operator


# Ex1:
# ====
# import time
# X1=1000 
# X2=3000 
# res1=X1+X2
# print("The result_set is:",res1)
# print()
# time.sleep(2)
# print('End of an application')

# x1=445
# sds=4545
# res=x1+sds
# print(res)
# res1=x1-sds
# print(res1)
# res2=x1*sds
# print(res2)

# Ternary operator:
# =================
# Ternary operator can be represent as if we are using one or more than 
# one variable with one more than one condition then it is said to be ternary
# operator.

# a=1000 
# b=900 
# max= a if a>b else b


# Ex1:
# ====
# import time
# a=eval(input("Enter the value of a:"))
# b=eval(input("Enter the value of b:"))
# max=a if a>b else b 
# print("Max_object is:",max)
# print()
# time.sleep(2)
# print('End of an application')


# Ex2:
# ====
# import time
# a=eval(input("Enter the value of a:"))
# b=eval(input("Enter the value of b:"))
# min=a if a<b else b 
# print("Min_object is:",min)
# print()
# time.sleep(2)
# print('End of an application')


# Ex3:
# ====
# import time
# a=eval(input("Enter the value of a:"))
# b=eval(input("Enter the value of b:"))
# c=eval(input("Enter the value of c:"))
# max= a if a>b and a>c else b if b>c else c 
# min= a if a<b and a<c else b if b<c else c 
# print("Max_Object is:",max)
# print()
# print("Min_object is:",min)
# print()
# time.sleep(2)
# print('End of an application')

# a=14
# b=16
# c=12
# max=a if a>b and a>c else b if b>c else c
# min=a if a<b and a<c else b if b<c else c
# print("Max_object is:",max)
# print("min object is:",min)
# print()


# x=122
# v=565
# min= x if x<v else v
# print("min object is:",min)
# max=x if x>v else v
# print("max is:",max)

# x=122
# v=565
# if x is x<v:                                
#     print("min object is:",x)
# else:
#     print("min object is :",v)
# print()
# if x is x>v:
#     print("max object is:",x)
# else:
#     print("max object is:",v)


# l=[1,2,5,5,5,52,82,312,54,2,4,5]
# j=[5,65,9215,1,85112,2,48,51,24,5,5]
# min= l if is l<j else j
# print("min")

# Chaining operators:
# ==================
# Python supports Chaining operators.The main objective of chaining operator is to perform complex comparision.While working with Chaining operator if one of the condition is false remaining all are false.Chaining operators return boolean values either True or False based on the condition.


# a=1000
# b=900
# c=800
# d=700
# e=600

# res1=a>b>c>d>e ---->True


# Ex1:
# ===
# import time
# a=eval(input("Enter the value of a:"))
# b=eval(input("Enter the value of b:"))
# c=eval(input("Enter the value of c:"))
# d=eval(input("Enter the value of d:"))
# e=eval(input("Enter the value of e:"))
# res1=a>b>c>d>e 
# print("The result_set is:",res1)
# print()
# time.sleep(2)
# print('End of an application')


# Ex2:
# ====
# import time
# a=eval(input("Enter the value of a:"))
# b=eval(input("Enter the value of b:"))
# c=eval(input("Enter the value of c:"))
# d=eval(input("Enter the value of d:"))
# e=eval(input("Enter the value of e:"))
# res1=a>b>c<d>e 
# print("The result_set is:",res1)
# print()
# time.sleep(2)
# print('End of an application')


# Ex3:
# ====
# import time
# a=eval(input("Enter the value of a:"))
# b=eval(input("Enter the value of b:"))
# c=eval(input("Enter the value of c:"))
# d=eval(input("Enter the value of d:"))
# e=eval(input("Enter the value of e:"))
# res1=a==b==c==d==e 
# print("The result_set is:",res1)
# print()
# time.sleep(2)
# print('End of an application')


# a=11
# b=11
# c=11
# d=11
# e=11
# res1=a==b==c==d==e
# print("the result_set is:",res1)
# print()

# # Ex4:
# ====
# import time
# a=eval(input("Enter the value of a:"))
# b=eval(input("Enter the value of b:"))
# c=eval(input("Enter the value of c:"))
# d=eval(input("Enter the value of d:"))
# e=eval(input("Enter the value of e:"))
# res1=a!=b!=c!=d!=e 
# print("The result_set is:",res1)
# print()
# time.sleep(2)
# print('End of an application')

a=11
b=18
c=114
d=212
e=1214
res2=a!=b!=c!=d!=e
print("the result_set is:",res2)


# Ex5:
# ===
# import time
# a=eval(input("Enter the value of a:"))
# b=eval(input("Enter the value of b:"))
# c=eval(input("Enter the value of c:"))
# d=eval(input("Enter the value of d:"))
# res1=a+b==c*d
# print("The result_set is:",res1)
# print()
# time.sleep(2)
# print('End of an application')

# a=14
# b=14
# c=14
# d=2
# res2=a+b==c*d
# print(res2)

