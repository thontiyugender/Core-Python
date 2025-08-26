# import time
# print("The result_set is:",77 & 7)
# print()
# time.sleep(2)
# print('End of an application')

# import time
# print("The result_set is:",77|7)
# print()
# time.sleep(2)
# print('End of an application')

# import time
# print("The result_set is:",77^7)
# print()
# time.sleep(2)
# # print('End of an application')

# print("the result_set is:",(6|7)&(2^3))


# print("the result_is:",(15&15)|(20|20))

# print("the result_set is:",(122|5545)&(114141^21))

# res1=print("the result_set is:",(122|5545)&(114141^21))
# res2=print("the result_set is:",(122|5545)&(114141^21))
# print()
# print(type(res1))
# print(type(res2))
# print(res1==res2)
# print(res1 is res2)
# print(res1 is not res2)
# if res1 and res2 is  str():
#     print("yes")
# else:
#     print("no")
# if (res1==res2):
#     print("the values are equal")
# else:
#     print("they are different")
# if(52 is res1):
#     print("true")           
# else:
#     print("false")
# if (5576 is res2 and res1):
#     print("true")
# else:
#     print("false")
# if(res1 or res2==5576):
#     print('joke')
# elif(res1 and res2>5576):
#     print("prank")
# elif(res1 and res2!=5576):
#     print("hlo")
# else:
#     print("yug")

# Bitwise complement operator:
# ============================

# Ex1:
# ===
# import time 
# X1=100
# print(X1)
# X2=~X1 
# print()
# print(X2)
# print()
# time.sleep(2)
# print("End of an application")


# x1=131
# print(x1)
# x2=~x1
# print(x2)

# # Ex2:
# # ====
# import time 
# X1=-101
# print(X1)
# X2=~X1 
# print()
# print(X2)
# print()
# time.sleep(2)

# x1=-121
# print(x1)
# x2=-x1
# print(x2)

# Bitwise left_shift operator(<<)
# ===============================


# X1=20 

# X2=X1<<2


# 20   ---->   1 0  1 0  0
# adding two zero's left_side                0   0  1  0  1 0 0    
           
#                                                1  0  1  0 0 0 0

# X1=20
# X2<<3 
        
#                        1  0   1  0  0 
#                        0  0  0  1  0  1  0  0 
#                             1  0  1  0  0  0  0  0 


# Ex1:
# ===
# import time 
# X1=20 
# X2=X1<<3
# print("The result_set is:",X2)
# print()
# time.sleep(2)
# print('End of an application')



# Ex1:
# ===
# import time 
# X1=20 
# X2=X1<<2 
# print("The result_set is:",X2)
# print()
# time.sleep(2)
# print('End of an application')



# Bitwise Right_shift(>>):
# =======================

# X1=20 


# 20  ---->      1  0   1  0  0 
#                0  0  1  0  1  0 0
#                     0  0  0  0  1  0   1


# Ex1:
# ===
# import time 
# X1=20 
# X2=X1>>2
# print("The result_set is:",X2)
# print()
# time.sleep(2)
# print('End of an application')



# X1=7
# X2=X1<<2 

# Integer number is  = 7
# Binary number   =  111
# Adding 2'0  ----->   00111
# Left_shift                       11100


# While doing rigt_shitf operation we are getting the different O/P

# Binary number  =   111 
#                     11100
#                    Right_shift 11001 ----> 25

# sift operators if it 1's output is changing

# Ex1:
# ====
# import time 
# X1=7 
# X2=X1>>2 
# print(X2)
# print()
# time.sleep(2)
# print('End of an application')


# Note:
# =====
# if zero's output will be same

# if one's output will be difference

# x1=24
# x2=x1>>3
# print(x2)

# x1=255
# x2=x1>>5
# print(x2)

# x1=5465
# x2=x1<<4
# print(x2)

# x1=64554
# x2=x1<<2
# print(x2)

# x1=58
# x2=x1<<3
# print(x2)
# x3=x1>>3
# print(x3)

# How to represent binary number in python?
# ========================================

# 0b10101

# or

# 0B111

# Ex1:
# ===
# import time 
# X1=0b101 
# X2=0B111 
# print("The value of X1 is:",X1)
# print()
# print("The value of X2 is:",X2)
# print()
# time.sleep(2)
# print('End of an application')


# bin():
# ======
# Converting a number into binary number


# Ex1:
# ===
# import time 
# X1=int(input("Enter the value of X1:"))
# X2=bin(X1)
# print("The integer value is:",X1)
# print()
# print("The Binary value is:",X2)
# print()
# time.sleep(2)
# print('End of an application')


# x1=0b1010
# x2=0B1101
# print("the result set is:",x1)
# print("the result set is:",x2)

# x1=0b111101
# x2=0B1010111
# print("the result set is:",x1)
# print("the result set is:",x2)

# x1=15
# x2=bin(x1)
# print("the result set is:",x2)

# x1=int(input("enter the value:"))
# x2=bin(x1)
# print("the integer value of x1:",x1)
# print("the binary value is:",x2)


# x1=int(input("enter the value:"))
# x2=bin(x1)
# print("the binary value is:",x2)

# x=0x12545
# print(x)

# x=0o1211
# print(x)

# oct():
# ======
# It is a predefine function in python.The main objective of oct() function is 
# to covert the number and binary number into octal number 

# Ex1:
# ====
# import time 
# X1=eval(input('Enter the number:'))
# print("Integer_value is:",X1)
# print()
# X2=oct(X1)
# print("Octal_number is:",X2)
# print()
# time.sleep(2)
# print('End of an application')


# x1=int(input("enter the value :"))
# x2=oct(x1)
# print(x2)
# print()

# x1=54
# x2=oct(x1)
# print("the integer value is:",x1)
# print("the ooctal value is:",x2)

# print()
# x1=0o2112
# print(x1)

# # Ex2:
# ===
import time 
# X1=0B111 
# X2=oct(X1)
# print("The value of X2 is:",X2)
# print()
# time.sleep(2)
# print('End of an application')

# x=0b111
# y=int(x)
# print(y)
# x2=0o7
# m=int(x2)
# print(m)


import time 
X1=0B10101000
X2=oct(X1)
x3=hex(X1)
print("The octal value of X1 is:",X2)
print()
print("the hex valueof x1:",x3)
time.sleep(2)
print('End of an application')

X1=0b10101000
y=int(X1)
print(y)
x2=0o250
m=int(x2)
print(m)
x3=0xa8
l=int(x3)
print(l)



# x1=0b11101
# x2=oct(x1)
# print(x2)

# m1=0O154
# m2=bin(m1)
# print(m1)
# print(m2)

# How to represent Hexa_decimal number in python:
# ===============================================
# We can represent hexa_decimal number as follow

# 0--9
# 10 --- A or a 
# 11 --- B or b 
# 12 ---- C or c
# 13 ---- D or d 
# 14 ---- E or e 
# 15  --- F or f


# x1=0x12
# print(x1)
# x2=0xacd
# print(x2)
# x=0xadc
# print(x)

# x1=0xa
# print(x1)
# x2=0xab
# print(x2)





# 0Xabcd 
# or
# 0xABCD
# or
# 0XRRR ---->In_valid hexa_decimal number
# or
# 0XaBcD


# Ex1:
# ====
# import time 
# Y1=0XA 
# Y2=0xa 
# Y3=0XAaBb 
# Y4=0x123456789 
# print(Y1)
# print()
# print(Y2)
# print()
# print(Y3)
# print()
# print(Y4)
# print()
# time.sleep(2)
# print('End of an application')


# hex():
# =====
# It is a predefine function in python coverts the python objects

#         from number to hexa_decimal number
#         from binary to hexa_decimal number 
#         from octal to hexa_decimal number 


# Ex1:
# ===
# import time 
# Z1=eval(input('Enter the value of Z1:'))
# print("The value is:",Z1)
# print()
# Z2=hex(Z1)
# print("Hexa_decimal number is:",Z2)
# print()
# time.sleep(2)
# print('End of an application')


# Ex2:
# ===
# import time 
# Z1=eval(input('Enter the value of Z1:'))
# print("Integer number is:",Z1)
# print()
# Z2=bin(Z1)
# Z3=oct(Z1)
# Z4=hex(Z1)
# print("Binary number is:",Z2)
# print()
# print("Octal_Number is:",Z3)
# print()
# print('Hexa_decimal number is:',Z4)
# print()
# time.sleep(2)
# print('End of an application')



