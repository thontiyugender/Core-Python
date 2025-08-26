"""right angle triangle pattern"""

n=5
for i in range(n):
    for j in range(i + 1):
        print("*",end="")
    print()


"""inverted right angle triangle"""
# n=5
# for i in range(n, 0 ,-1):
#     for j in range(i):
#         print("*", end="")
#     print()


"""pyramid pattern"""


# n=5
# for i in range(n):
#     print(" " * (n - i - 1)+"*" * (2 * i -1))


"""inverted pyramid pattern"""
# n=5 
# for i in range(n, 0, -1 ):
#     print(" " * (n-i)+ "*" *(2*i-1))


'''Diamond pattern'''
# # top half
# n=5
# for i in range(n):
#     print(" " * (n - i -1) + "*" * (2*i+1))

# # bottom half
# for i in range (n -2,-1,-1):
#     print(" " * (n-i-1) + "*" * (2*i+1))


'''number pattern'''
# n=5
# num=1
# for i in range(n):
#     for j in range(i+1):
#         print(num, end=" ")
#         num+=1
#     print()

'''Alphabet Pattern'''

# n=5
# char='A'
# for i in range(n):
#     print(" " * (n-i -1)+char * (2 * i + 1))
#     char=chr(ord(char)+1)

'''hollow square pattern'''
# n=5
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n-1 or j==0 or j == n - 1 :
#             print("*", end="")
#         else:
#             print(" ",end="")
#     print()


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
