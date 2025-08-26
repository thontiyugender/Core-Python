# import time
# l1=[554,45,454,54,54,454,454,4]
# print()
# for x1 in l1:
#     print(x1,end=" ")      #TO USE SPACE WE HAVE TO USE END=" "
# print()
# time.sleep(1)
# print("End of an application")


# fibonacci series/
# 
def print_fibonacci_num(num):
    a,b=0,1
    if num<1:
        print("null")
    elif(num==1):
        print(a)
    elif num==2:
        print(a)
        print(b)
    elif(num>2):
        print(a)
        print(b)
        for i in range(num-2):
            c=a+b
            a,b=b,c
            print(c, end=" ")
print_fibonacci_num(int(input("enter the number:")))





# # import time 
# # S1=0
# # for y1 in [1001,1002,1003,1004,1005,1006,1007,1001,1002,1003]:
# #     S1=S1+y1 
# # print("The sum of list is:",S1)
# # print()
# # time.sleep(2)
# # print("End of an application")


# # import time
# # l1=dict{gh:5565,hgfgugf:665565,duhfhf:"hdyfgydgff"}
# # for x1 in l1:
# #     print(l1)
# # print()
# # time.sleep(2)
# # print("End of an application")

# # import time
# # sum=1
# # while(True):
# #     print(sum)
# #     sum+=1
# # print()
# # time.sleep(1)
# # print("end")

# # import time
# # sum=1
# # while(False):
# #     print(sum)
# #     sum+=1
# # print()
# # time.sleep(1)
# # print("end")

# # import time
# # sum=1
# # while(0):
# #     print(sum)
# #     sum+=1
# # print()
# # time.sleep(1)
# # print("end")

# # import time
# # l1=[1,2,3,4,5,6]
# # b=0
# # while(b<len(l1)):
# #     print("indexing values are:",l1[b])
# #     b+=1
# # print()
# # time.sleep(1)
# # print("end")


# # import time
# # l1=[1,2,3,4,5,6]
# # b=0
# # while(b<len(l1)):
# #     print(b,"---",l1[b])
# #     b+=1
# # print()
# # time.sleep(1)
# # print("end")

# # number=1
# # while number<=9:
# #     if number % 2 != 0:
# #         print(number)
# #         number+=1


# # m1=[1,2,3,4,5,6,7,8,9]
# # y=0
# # while(m1[y]%2==1):
# #     print(m1)
# # print()



# # l1=[1,2,3,4,5]
# # l2=[1,2,6,5,8]
# # combined_list=list(set(l1+l2))
# # print(combined_list)



# # import time
# # h=[1,2,3,4,5,6,7,8,9]
# # while(h%2!=0):
# #     print("odd numbers are:",h)
# # print()
# # time.sleep(1)
# # print("End of an application")

# # num=1
# # print("Odd numbers from 1 to 9:")--
# # while num <= 9:
# #     if num % 2 != 0:
# #         print(num)
# #     num += 1


# # import time 
# # ABC=12000 
# # print("Value is:",ABC)
# # print()
# # print("Address is:",id(ABC))
# # print()
# # print("Data type is:",type(ABC))
# # print()
# # time.sleep(2)
# # print('End of an application')


# # import time
# # l1=[1,2,3,4,5,6,7,8,9]
# # a=0
# # s1=0
# # while(a<len(l1)):
# #     s1=s1+l1(a)
# #     a+=1
# # print("sum of the list:")
# # print() 
# # time.sleep(1)
# # print("End of an application")

# import time
# l1=[1,2,3,4,5,6,7,8,9]
# l2=[]
# for i in range(len(l1)):
#     if(l1[i]%2==1):
#        l2.append(l1[i])
       
# print(l2)
# time.sleep(1)
# print("End of an application")

# # fruits=["apple","orange","guava"]
# # for fruit in fruits:
# #     print(fruit)
# #     if fruit=="guava":
# #         print("found guava")
# #         break


# # num=[1,3,2,52,562,65,2,565,55]
# # for i in num:
# #     if i>500

# l=(1,2,3,4,5,6)
# print(len(l))
# a=0
# b=0
# while (a<len(l)):
#     b=b+l[a]
#     a+=1
# print(b)

# import time
# for x1 in range(9):
#     if(x1==5):
#         print("end the sentences")
#         break
#     print("the preffered values are:",x1)
# print()
# time.sleep(1)
# print("End of an application")

# import time
# l1=[112,113,114,116,115,900,2,3,4,5,6,7]
# for x1 in l1:
#     if x1>890:
#         print("welcome to mayura technologies")
#         continue
#     print("list_processing are:",x1)
# print()
# time.sleep(2)
# print("end of an application")

# a=[1,2,3,4,5]
# # for i in a:
# #     if i==4 :
# #         print("list is oveer")
# #         continue
# #     print("pver")

# import time
# l1=[112,113,114,116,115,900,2,3,4,5,6,7]
# for x1 in l1:
#     if x1>890:
#         print("welcome to mayura technologies")
#         continue
#     print("list_processing are:",x1)
# else:
#     print("all iitems are successfully executed...")
# print()
# time.sleep(2)
# print("end of an application")


# import time
# l1=[112,113,114,116,115,2,3,4,5,6,7]
# for x1 in l1:
#     if x1>890:
#         print("welcome to mayura technologies")
#         continue
#     print("list_processing are:",x1)
# else:
#     print("all iitems are successfully executed...")
# print()
# time.sleep(2)
# print("end of an application")


# def Test_case1():
#    pass
# def Test_case2():
#    pass
# def Test_case3():
#    pass
# def Test_case4():
#    pass
# def Test_case5():
#    pass
# if(__name__=="__main___"):
#    Test_case1()
#    Test_case2()
#    Test_case3()
#    Test_case4()
#    Test_case5()
# print()


# def Test_case1():
#    print("jkcjcnj")
# def Test_case2():
#    pass
# def Test_case3():
#    pass
# def Test_case4():
#    print("sndbshsb")
# def Test_case5():
#    pass
# if(__name__=="__main___"):
#    Test_case1()
#    Test_case2()
#    Test_case3()
#    Test_case4()
#    Test_case5()
# print()

# import time
# def Test_case1():
#     print("jfewf")
#     return("know your place")
# if (__name__=="__main__"):
#    Test_case1()
#    print()
#    Test_case1()
#    print()
#    Test_case1()
#    print() 
#    print(Test_case1())
# time.sleep(1)
# print("end of an application")

# import time 
# def Test_Case1():
#     print("Welcome to IHUB_APP_DEVELOPMENT")
#     print()
#     return "Welcome to Mobile_application_development"
# if(__name__=="__main__"):
#     Test_Case1()
#     print()
#     Test_Case1()
#     print()
#     Test_Case1()
#     print()
#     print(Test_Case1())
# print()
# time.sleep(2)
# print('End of an application')

# def Test_case1():
#     print("fjgh")
#     print()
#     return("gfgf")
# if(__name__=="__main__"):
#     Test_case1()
#     Test_case1()
#     Test_case1()
#     print(Test_case1())
# # print()

# def test_case(**ihub):
#     for y1 in ihub :
#         print(y1)      # IT IS FOR ruff work wrong code by me
# if(__name__=="__main__"):
#     print("ihub")
# print()    
            
# numbers = [1, 5, 3, 2, 4]
# sorted_numbers = sorted(numbers)
# print(sorted_numbers) 
# print()

# print()
# strings = ['a', 'c', 'b', 'd']
# sorted_strings = sorted(strings)
# print(sorted_strings) 
# print()

# tuple = (1, 5, 3, 2, 4)
# sorted_tuple = sorted(tuple)
# print(sorted_tuple) 
# print()

#  #Sort a dictionary
# dictionary = {'a': 1, 'c': 3, 'b': 2, 'd': 4}
# sorted_dictionary = sorted(dictionary)
# print(sorted_dictionary) 
# print()

# Sort a list of objects

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __repr__(self):
#         return f'{self.name} ({self.age})'

# people = [Person('Alice', 25), Person('Bob', 30), Person('Carol', 28)]
# print()

# # Sort by age
# sorted_people = sorted(people, key=lambda person: person.age)
# print(sorted_people) 
# print()

# # Sort by name
# sorted_people = sorted(people, key=lambda person: person.name)
# print(sorted_people) 

# num=1
# while num<=5:
#     print(num)
#     num +=1       #if we dont use num +=1, it will give inifnite values... 2nd one is example..
 
# num=1
# while num<=5:
#     print(num)



# a=int(input("enter the value:"))
# b=int(input("enter the value:"))
# res1=a+b
# print(res1)


# Y=[1,2,3,4,5,6,7,8,9]
# l=[]
# for m in range(len(Y)):
#     if(Y[m]%2==0):
#         l.append(Y[m])
#         print("even numbers are:",Y[m])
#     else:
#         print("odd numbers are :",Y[m])

# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# a=a+b
# b=a-b
# a=a-b
# print("After the swap:",a,b)
# print("a=",a)
# print("b=",b)

# # Input numbers
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))

# # Swapping values without a temporary variable
# a = a + b
# b = a - b
# a = a - b

# # Displaying the result
# print("After the swap:")
# print("a =", a)
# print("b =", b)




''' swapping A NUMBER:'''


# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))

# # Displaying the entered numbers
# print("Before the swap: a = %d, b = %d" % (a, b))

# # Swapping values without a temporary variable
# a = a + b
# b = a - b
# a = a - b

# # Displaying the swapped values
# print("After the swap: a = %d, b = %d" % (a, b))