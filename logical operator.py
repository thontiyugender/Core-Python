# # Python supports Logical operators.The main objective of logical operators to perform logical operations as per the application reqn.Following are the Logical operators in Python.

# # ->Logical and ---- > and 
# # ->Logical or -----> or 
# # ->Logical not ----->  not


# # ->Logical and ---- > and:
# # ==========================
# # True ---- > 1
# # False ---->  0 

# # X1     X2      X1 and X2
# # =========================
# # 1      0          0
# # 0      1          0                           # only true is true= output
# # 1      1          1
# # 0      0          0
# # ==========================

# # Logical and operator is meant for to provide the security to the application

# import time
# print("===WELCOME TO MAYURA TECHNOLOGIES===")
# username=input("enter the username:")
# password=input("enter the password:")
# print()
# if(username=="yugender" and password=="131141191"):
#     print(username,password,":login sucessfully...")
# else:
#     print(username,password,":access denied")
# print()
# time.sleep(1)
# print("End of an application")
# print()

# print("==my details==")
# name=input("enter name:")
# classes=int(input(enter classes:))
# print()
# if(name=="raju" and classes==10):                                        #doubt.............................
#     print(name,classes,":joined the classes")
# else:
#     print(name,classes,":not joined the classes")

# print("==my details==")
# name=input("enter name:")
# classes=input("enter classes:")
# print()
# if(name=="raju" and classes==10):
#     print(name,classes,":joined the classes")
# else:
#     print(name,classes,":not joined the classes")


# print("==my details==")
# name=input("enter name:")
# classes=int(input("enter classes:"))
# print()
# if(name=='raju' and classes==10):                                        #doubt.............................
#     print(name,classes,":joined the classes")
# else:
#     print(name,classes,":not joined the classes")


# # # Ex1:
# # # ====
# # import time 
# # print("=====Welcome to IHUB_International_Bank====")
# # username=input("Enter the username:")
# # password=input("Enter the password:")
# # if(username=="rahul_12345" and password=="RA_12345"):
# #     print(username,password,":Login successfully ....")
# # else:
# #     print(username,password,":In_valid user ....")
# # print()
# # time.sleep(2)
# # print("End of an application") 


# # x=1
# # y=2
# # z=4
# # if(x>y and y>z):
# #     print("x is greater than y,z")
# # else:
# #     print("x is not greater than y,z")
# #     print()


# # ->Logical or -----> or :
# # ========================
# # True  ---->   1 
# # False  ---->  0                IN LOGICAL OR OPERATOR IF one condition is true it is true......


# # X1     X2      X1 or X2
# # =========================
# # 1      0          1
# # 0      1          1
# # 1      1          1
# # 0      0          0
# # ==========================

# # import time
# # username=input("enter the username:")
# # password=input("enter the password:")
# # repassword=input("re enter the the passsword:")
# # p1=input("enter the password:")
# # p2=input("re enter the password:")
# # if(username=="yugender"or password=="thonti" or repassword==131141191 and p1=="yugender" and p2==131141191):
# #     print("login successfully.....")
# #     print("username is:",username)
# #     print("password is:",password)
# #     print("repassword is:",repassword)
# #     print("p1 is:",p1)
# #     print("p2 is:",p2)

# # # else:
# # #     print("access denied")



# import time 
# fname=input('Enter the fname:')
# lname=input('Enter the lname:')
# username=input('Enter the username:')
# P1=input('Enter the Password:')
# P2=input('Enter the Confirm_password:')
# if(fname=="yugender" or lname=="thonti" or username==131141191 and P1=="J_12345" and P2=="J_12345"):
#     print("====New User_Information====")
#     print("Fname is:",fname)
#     print("Lname is:",lname)
#     print("Username is:",username)
#     print("Password is:",P1)
#     print("Confirm Password is:",P2)
#     print()
# else:
#     print("Username/P1/P2 are requried ....")

# # # print()
# # # time.sleep(2)
# # # print("End of an application")

# # a = 10
# # b = -10
# # c = 0
# # if a > 0 or b > 0:
# #     print("Either of the number is greater than 0")
# # else:
# #     print("No number is greater than 0")
# # if b > 0 or c > 0:
# #     print("Either of the number is greater than 0")
# # else:
# #     print("No number is greater than 0")

# # a=1
# # b=231
# # c=11
# # if a>11 or b<11:
# #     print("both are not higher than c")
# # else:
# #     print("either of them  greater than c")
# # if b<c or c<a:
# #     print("c is greater than a and less than b")
# # else:
# #     print("c is not greater than either of them")

    
# a=1
# b=231
# c=11
# if a>11 or b<11:
#     print("both are not higher than c")
# else:
#     print("either of them  greater than c")
# if b>c or c>a:
#     print("c is greater than a and less than b")
# else:
#     print("c is not greater than either of them")


# #     logical not operator:
# # =====================
# # True --->False 
# # False  ----> True


# # Ex1:
# # ====
# # import time 
# # X1=True 
# # print(X1)
# # print()
# # print(type(X1))
# # print()
# # X2=not X1 
# # print(X2)
# # print()
# # print(type(X2))
# # print()
# # time.sleep(2)
# # print('End of an application')


# # x1=11
# # x2=44
# # print(x1)
# # print()
# # print(type(x1))
# # x2=not x1
# # print(x2)
# # print(type(x2))


# # x1=11
# # print(x1)
# # print()
# # print(type(x1))       #if a boolean value is true if we use not operator it print false.....
# # x2=not x1 
# # x3=not x2
# # print(x2)
# # print(type(x2))
# # print(x3)
# # print(type(x3))

a = 10
if not a:
    print("Boolean value of a is True")
if not (a % 3 == 0 or a % 5 == 0):
    print("10 is not divisible by either 3 or 5")
else:
    print("10 is divisible by either 3 or 5")

L=[1,2,3,4,5,67,8,5,1,2,4,5,53,8]
n=[1,2,3,4,5,67,8,5,1,2,4,5,53,8]
res=L==n
print(res)
res1=not res
print(res1)


# # identity operator
# # =================
# # Specail type of operators:
# # =========================
# # Python supports Special types of operators.Following are the STO in Python

# # which are as follows

# # ->Identity operator
# # ->Membership operaor


# # ->Identity operator:
# # ====================
# # It is a STO in python.The main objective of Identity operators is meant for 
# # address comparsion return boolean values after checking condition.Following
# # are the Identity operators

# # ->is operator          in list WE GET FALSE,in tuple we get true
# # ->is not operator       in list  WE GET  TRUE,in tuple we get false

# # L1=[1,2,3,4,5,1,1,1,1,1,1]---->id(L1)----> 12345
# # L2=[1,2,3,4] ---->id(L2)---->112231


# # T1=(1,2,3,4) ---->id(T1) ----> 12
# # T2=(1,2,3,4) ---->id(T2) ----->12

# # T1=(1,2,3,4) ---->id(T1) ----> 12
# # T2=(1,2,3) ---->id(T2) ----->13

# import time
# l1=[1,2,3,4,5]
# l2=[1,2,3,4,5]
# print()
# print(l1)
# print()
# print(l2)
# print(id(l1))
# print(id(l2))
# print()
# print("===using identity operators====")
# print("the result_set is:",l1 is l2)
# print()
# print("the data type is:",type(l1 is l2))
# print()
# print("the result_set is:",l1 is not l2)
# print()
# print("the data type is:",type(l1 is not l2))
# print()
# time.sleep(1)
# print("End of an application")

# import time
# l1=(1,2,3,4,5)
# l2=(1,2,3,4,5)
# print()
# print(l1)
# print()
# print(l2)
# print(id(l1))
# print(id(l2))
# print()
# print("===using identity operators====")
# print("the result_set is:",l1 is l2)
# print()
# print("the data type is:",type(l1 is l2))
# print()
# print("the result_set is:",l1 is not l2)
# print()
# print("the data type is:",type(l1 is not l2))
# print()
# time.sleep(1)
# print("End of an application")


# # import time 
# # L1=(1,2,3,4)
# # L2=(1,2,3,4,5)
# # print("====Values====")
# # print(L1)
# # print()
# # print(L2)
# # print()
# # print("====Addresses=====")
# # print(id(L1))
# # print()
# # print(id(L2))
# # print()
# # print("====Using identity operators====")
# # print("The result_set is:",L1 is L2)
# # print()
# # print("The data type is:",type(L1 is L2))
# # print()
# # print("The result_set is:",L1 is not L2)
# # print()
# # print("The data type is:",type(L1 is not L2))
# # print()
# # time.sleep(2)
# # print('End of an application')

# import time
# l1=chr(96),chr(68),chr(66)
# l2=chr(96),chr(68),chr(66)
# print("===values===")
# print(l1)
# print(l2)
# print("====addresses====")
# print(id(l1))
# print(id(l1))
# print("the result_set is:",l1 is l2)
# print()
# print("data type is:",type(l1 is l2))
# print()
# print("the result_set is:",l1 is not l2)
# print()
# print("the data type is:",type(l1 is not l2))
# print()
# time.sleep(1)
# print("End of an application")

# import time 
# L1=(chr(65),chr(66),chr(67))
# L2=(chr(65),chr(66),chr(67))
# print("====Values====")
# print(L1)
# print()
# print(L2)
# print()
# print("====Addresses=====")
# print(id(L1))
# print()
# print(id(L2))
# print()
# print("====Using identity operators====")
# print("The result_set is:",L1 is L2)
# print()
# print("The data type is:",type(L1 is L2))
# print()
# print("The result_set is:",L1 is not L2)
# print()
# print("The data type is:",type(L1 is not L2))
# print()
# time.sleep(2)
# print('End of an application')


# l1=(1,2,3,4.5,6)
# l2=(1,2,3,4,5,6,7)
# print(l1 is not l2)
# print(l1 is l2)

# import time 
# L1=('A','B','C')
# L2=('A','B','C')
# print("====Values====")
# print(L1)
# print()
# print(L2)
# print()
# print("====Addresses=====")
# print(id(L1))
# print()
# print(id(L2))
# print()                                                                                                            
# print("====Using identity operators====")
# print("The result_set is:",L1 is L2)
# print()
# print("The data type is:",type(L1 is L2))
# print()
# print("The result_set is:",L1 is not L2)
# print()
# print("The data type is:",type(L1 is not L2))
# print()
# time.sleep(2)
# print('End of an application')


# import time 
# L1=(1,2,3,4,5)
# L2=(1,2,3,4,5)
# print("====Values====")
# print(L1)
# print()
# print(L2)
# print()
# print("====Addresses=====")
# print(id(L1))
# print()
# print(id(L2))
# print()
# print("====Using identity operators====")
# print("The result_set is:",L1 is L2)
# print()
# print("The data type is:",type(L1 is L2))
# print()
# print("The result_set is:",L1 is not L2)
# print()
# print("The data type is:",type(L1 is not L2))
# print()
# time.sleep(2)
# print('End of an application')