# ->Comprehension:
# ===============
# Python supports Comprehesion.It can be represent as if we are using one or
# more than one expresion with one or more than one condition then it is said
# to be comprehension.Comphrehension is applicable for following data type

# ->List Comprehension
# ->Tuple Comphrehension
# ->Set  Comprehension
# ->Dict Comprehension


# ->List Comprehension:
# ====================

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list. 
# Example: Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.


# Ex1:
# ===
# import time 
# L1=[x*x for x in range(10)]
# print(L1)
# print()
# print(type(L1))
# print()
# time.sleep(1)
# print('End of an application')
# print()

# numbers = [1, 2, 3, 4]
# squared_numbers = [number * number for number in numbers]
# print(squared_numbers)  # Output: [1, 4, 9, 16]
# print()

# you=[1,52,642,98,878,9998,6,5662,55]
# add=[you+you for you in you]
# print(add)
# print()

# nippu=[1,2,53,64,15,26,9871,1,32,48,76,9]
# fire=[nippu*5 for nippu in nippu]
# print(fire)


# c=[1,4,5,3,6,4,7,8,9,4,2,6]
# mr=[]
# e=[]
# for i in range(len(c)):
#     if (c[i]%2==0):
#         mr.append (c[i])
#     else:
#         e.append(c[i])
# print("even numbers are:",c[i])
# print("odd numbers are:",c[i])

# m=[1,23,4,55,68,78899,89,12,114]
# e=[]#it is used for the adding the elements
# o=[]
# for i in range(len(m)):
#     if(m[i]%2==0):
#         e.append(m[i])#append() is predefined function in list .it used for adding the elements in new list at position of last
#     else:
#         o.append(m[i])       
# print()
# print(f"even number of list {e}")
# print(f"odd number of list {o}")





# Ex2:
# ====
# import time 
# L1=[x*x for x in range(10) if x%2==0]
# print(L1)
# print()
# print(type(L1))
# print()
# time.sleep(2)
# print('End of an application')

# L=[I*I for I in range (22)]
# print(L)
# print(type(L))



# import time 
# L1=[x*x+1000 for x in range(10) if x%2==0]
# print(L1)
# print()
# print(type(L1))
# print()
# time.sleep(2)
# print('End of an application')


# yu=[x*x-10 for x in range (22) if x%2==0]
# print(yu)
# print(type(yu))

# print()
# p=[h*h+1000 for h in range(12) if h%2==0]
# print(p)
# print(type(p))


x=[x+x for x in range (13)if x%2==0]
print(x)



# for x1  in range (26):
#     if(x1%2==0):
#         print("even munbers are:",x1)
#         print(x1.add(100))
#     else:
#         print("odd number are:",x1)


# for x1  in range (26):
#     if[x1%2==0]:
#         print["even munbers are:",x1]
#         x1.append(100)
#     else:
#    


# c=[1,4,5,3,6,4,7,8,9,4,2,6]
# mr=[]
# e=[]
# for i in range(len(c)):
#     if (c[i]%2==0):
#         mr.append (c[i])
#     else:
#         e.append(c[i])
# print("even numbers are:",c[i])
# print("odd numbers are:",c[i])

# x1=[1,1,45,5,5,25,52,56,4,8,3]
# for i in range(len(x1)):
#     if (x1[i]%2==0):
#         if(x1[i]<=64):
#             print("even numbers are :",x1[i])
#         else:
#             print("odd numbers are:",x1[i])


# x1=[1,1,45,5,5,25,52,56,4,8,3]
# for i in range(len(x1)):
#     if (x1[i]%2==0):
#         print("even numbers are :",x1[i])
#     else:
#         print("odd numbers are:",x1[i])
# print()

# m=[2,5,58,466,694,231,456]
# for i in range (len(m)):
#     if(m[i]%2==0):
#         print("even numbers :",m[i])
#     else:
#         print("odd numbers are:",m[i])

# u=[1,5,2,3,6,4,7,8,6,95,41,2,3,6]
# m=[]
# h=[]
# for i in range(len(u)):
#     if[u[i]%2==0]:
#         m.append(u[i])
#     else:
#         h.append(u[i])
# print("even:",u[i])
# print("odd:",u[i])


# c=[1,4,5,3,6,4,7,8,9,4,2,6]
# mr=[]
# e=[]
# for i in range(len(c)):
#     if (c[i]%2==0):
#         mr.append(c[i])
#     else:
#         e.append(c[i])
# print()
# print("even numbers are:",c[i])
# print("odd numbers are:",c[i])
# print()

# c=[1,4,5,3,6,4,7,8,9,4,2,6]
# mr=[]
# e=[]
# for i in range(len(c)):
#     if (c[i]%2==0):
#         mr.append(c[i])
#     else:
#         e.append(c[i])
# print()
# print("even numbers are:",mr)
# print("odd numbers are:",e)
# print()


# l=[1,23,4,55,67,78899,89]
# for i in range(len(l)):
#     if(l[i]%2==0):
#         print("even numbers are:",l[i])
#     else:
#         print("odd numbers are:",l[i])
# print()

# my_list = [1, 4, 2, 8, 5]

# # Check if a specific value exists in the list
# if 8 in my_list:
#     print("8 is present in the list.")

# # Check if an element meets a certain condition
# for number in my_list:
#     if number % 2 == 0:
#         print(f"{number} is even.")



# Tuple comprehension:
# ====================
# Python supports Tuple Comprehension.It returns generator object with generator class.

# Ex1:
# ===
# import time 
# T1=(x*x for x in range(10))
# print(T1)
# print()
# print(type(T1))
# print()
# time.sleep(2)
# print('Endof an application')


# t1=(x*x for x in range (11))
# print(t1)
# print()
# print(type(t1))
# print()


# f1=(l*l for l in range (1500) if l%2==0)
# print(*f1)
# print()
# print(type(f1))

# Ex2:
# ====
# import time 
# T1=(x*x for x in range(10))
# print(*T1)
# print()
# print(type(T1))
# print()
# time.sleep(2)
# print('Endof an application')


# Ex3:
# ===
# import time 
# T1=(x*x for x in range(10))
# for x1 in T1:
#     print(x1)
# print()
# print(type(T1))
# print()
# time.sleep(2)
# print('Endof an application')

# k1=(p+p for p in range(150))
# k=[]
# for p in k1:
#     if(p%2==0 and p<=64):
#         print(p,end=" ")
# print()
# print(*k1)
# print(type(k1))
# print() 

# k1=(p+p for p in range(150))
# k=[]
# for p in k1:
#     if(p%2==0 and p<=64):  # updated by me using chat gpt code below
#         print(p,end=" ")

# print()


# #gggg
# k1 = (p + p for p in range(150))
# even_numbers = [num for num in k1 if num % 2 == 0 and num <= 64]      # chatgpt code
# print(even_numbers)


# Set comprehension:
# =================
# Python supports set comprehension.It can be represent as if we are
# using one or more than one expression with one or more than one
# condition inside the set data type then it is said to be set comprehension.


# Ex1:
# ===
# import time  
# S1={y1*y1 for y1 in range(1,11,1)}
# print(S1)
# print()
# print(type(S1))
# print()
# for x1 in S1:
#     print(x1)
# print()
# time.sleep(2)
# print('End of an application')

