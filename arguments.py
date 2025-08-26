# PYHTON FUNCTION ARGUMENTS:
# ==========================

# the arguments is a value,a variable,or an object that we pass to a function or method call..
# in python,there are four types of arguments allowed.

# 1.positional arguments
# 2.keyword arguments
# 3.default arguments
# 4.variable length arguments

# 1.positional arguments
# =======================

# Python supports Positional argument while working with functional programming 
# language.It can be represent as combination of formal parameters and actual parameters.Positional
# argument works based on position.

# def test(x1,x2,x3):
#     print("the value is:",x1)
#     print("the vlue is:",x2)
#     print("the value is:",x3)
# if(__name__=="__main__"):
#     test(1000,2000,3000)
# print()

# def test1(x3,x2,x1):
#     print("the value is:",x1)
#     print("the value is:",x2)
#     print("the value is:",x3)
# if(__name__=="__main__"):
#     test1(1000,2000,3000)
# print()

# Default argument:
# ===========
# Python supports Default argument while working with functional programming
# language.Default argument can be represent as if we are using one or more
# than one formal parameters with their value then it is said to be Default argument.
# While working with default argument default argument must be placed in last position.

# def room(eid=1001,ename,esal,design,company):
#     print("====EMPLOYEE DETAILS=======")
#     print("EID IS:",eid)
#     print("ename is:",ename)
#     print("esal is:",esal)
#     print("design is :",design)
#     print("company is:",company)
# if(__name__=="__main__"):
#     room("yugender",1000.00,"python","mayura_technologies")

# def room(ename,esal,design,company,eid=1001):
#     print("====employee details=====")
#     print("eid is:",eid)
#     print("ename is:",ename)
#     print("esal is:",esal)
#     print("company is:",company)
#     print("design is:",design)
# if(__name__=="__main__"):
#     room("yugender",10000.00,"mayura technologies","pythin")
# print()

# def Test_Case1(Eid=1001,Ename="Jessica",Esal=23000,Design="UI developer",Company="A_tech"):
#            print("-----Employee_Details-----")
#            print("Eid is:",Eid)
#            print("Ename is:",Ename)
#            print("Esal is:",Esal)
#            print("Design is:",Design)
#            print("Company is:",Company)
# if(__name__=="__main__"):
#         Test_Case1()


# def Test_Case1(Eid=1001,Ename="Jessica",Esal=23000,Design="UI developer",Company="A_tech"):
#            print("-----Employee_Details-----")
#            print("Eid is:",Eid)
#            print("Ename is:",Ename)
#            print("Esal is:",Esal)
#            print("Design is:",Design)
#            print("Company is:",Company)
# if(__name__=="__main__"):
#     Test_Case1(1005,"Priya",29000,"Developer","B_Tech")    
# print()

# def road(a,b,c=1000):
#     return a+b*c
# if(__name__=="__main__"):
#     print(road(2,5))
# print()

# def Test_Case1(a,b,c=1000):
#     return a+b*c 
# if(__name__=="__main__"):
#     print(Test_Case1(2,5,10))
# print()


# def Test_Case1(b,c=1000,a=1200):
#     return a+b*c 
# if(__name__=="__main__"):
#     print(Test_Case1(2))
# print()


# ->Keyword argument:
# ==============
# Python supports keyword argument while working with functional programming language.Keyword
# argumemt can be represent as if we are using actual parameters with their values then is said to 
# be keyword argument.

# def test_case1(sid,sname,subject,mark):
#     print("===student details===")
#     print("sid is:",sid)
#     print("sname is:",sname)
#     print("subject is:",subject)
#     print("marks is:",mark)
# if(__name__=="__main__"):
#     test_case1(sid=32322,sname="yugender",subject="python",mark=99)
# print()


# def texas(pid=1001,pname="apple",price=454556,company="iphone"):
#     print(pid,pname,price,company)
# if(__name__=="__main__"):
#     texas(pid=1002,pname="apple2",price=121122,company="mayura")
# print()

# ->Variable length argument:
# ==================
# Python supports Variable length argument which can be define or declare as * followed variable_name.
# The main objective of variable length argument is read zero or more than one  number of arguments and
# perform the operations as the application reqn.Variable length arguments returns data or information in 
# Tuple format.

# def Test_Case1(*variable_name):
#             ------

# def Test_Case1(*obj1):
#     print(obj1)
# if(__name__=="__main__"):
#     Test_Case1()
#     print()
#     Test_Case1(1000)
#     print()
#     Test_Case1(1000,2000)
#     print()
#     Test_Case1(1000,2000,3000)
#     print()
#     Test_Case1(1000,2000,3000,4000)
# print()



# def Test_Case1(*obj1):
#     for x1 in obj1:
#         print(x1)
    
# if(__name__=="__main__"):
#     Test_Case1()
#     print()
#     Test_Case1(1000)
#     print()
#     Test_Case1(1000,2000)
#     print()
#     Test_Case1(1000,2000,3000)
#     print()
#     Test_Case1(1000,2000,3000,4000)
# print()


# def raju(*a):
#     b=0
#     for c in a:
#         b=b+c
#     print("sum is:",b)
# if(__name__=="__main__"):
#     print()
#     raju(100)
#     print()
#     raju(100,200)
#     print()
#     raju(100,200,300)

# def Test_Case1(*obj1):
#     S1=0 
#     for x1 in obj1:
#         S1=S1+x1 
#     print("Sum of any_number of arguments:",S1)
# if(__name__=="__main__"):
#     Test_Case1()
#     print()
#     Test_Case1(1000)
#     print()
#     Test_Case1(1000,2000)
#     print()
#     Test_Case1(1000,2000,3000)
#     print()
#     Test_Case1(1000,2000,3000,4000)
# print()

# def Test_Case1(*obj1):
#     for x1 in obj1:
#         print(x1) 
# if(__name__=="__main__"):
#     Test_Case1("Rahul","Sharma","rahul_12345","RA_12345","RA_12345","rahul@gmail.com")
#     print()
#     Test_Case1("Ajay","Verma","ajay_54321","AJ_12345","AJ_12345","ajay@gmail.com")
# print()

# def data(*obj1):
#     for x1 in obj1:
#         print(x1)
# if(__name__=="__main__"):
#     data("yugender","yugi","yug_123","yuge_12314")
#     print()
#     data("information","data","info_123","data_1234")
#     print()
# print()

# ->Keyword variable length argument:
# =======================
# Python supports KVLA.We can define or declare as ** followed by variable_name.The main objective
# of keyword variable length argument to read zero or more than one number arguments in key and value 
# format.

# def Test_Case1(**variable_name):
#        -----


# def Test_Case1(**z1):
#     for x1,x2 in z1.items():
#         print(x1,"-",x2)
# if(__name__=="__main__"):
#     Test_Case1(Pid=1001,Pname="Mobile_1",Price=21000)
#     print()
#     Test_Case1(Pid=1002,Pname="Mobile_2",Price=23000)
# print()


# def test_case2(**y1):
#     for x1,x2 in y1.items():
#         print(x1,"--",x2)
# if(__name__=="__main__"):
#     test_case2(pid=1001,pname="apple",price=10000)
#     print()
#     test_case2(pid=1002,pname="iphone",price=23000)


def test_case2(*y1):
    for x1,x2 in y1.items():     ##.. it will not execute values....
        print(x1,"--",x2)
if(__name__=="__main__"):
    test_case2(pid=1001,pname="apple",price=10000)
    print()
    test_case2(pid=1002,pname="iphone",price=23000)

