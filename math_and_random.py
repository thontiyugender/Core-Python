# # math module:
# # ============
# it is a predefine module in python. the main objectiive of math module is to 
# perform complex operations for mathematics we can go for module..
    

# import math 
# print(math.sqrt(9))
# print()
# print(math.sqrt(16))
# print()


# from math import *
# print(sqrt(64))
# print()
# print(sin(45))
# print()
# print(cos(90))
# print()

# import math
# print("====sub_modules=====")
# print()                          ####...to know the values of modules...
# print(dir(math))
# print()
# print("==================")


"""working on random module:
==============================
IT is a predefine module in python.the main objective of random module is perform random 
operations as per the application requirement."""


# import time
# from random import*
# print("======sub modules=========")
# print()
# print(dir(random))



# While working with random_module we do have following functions which 
# are as follows:
# ================================================

# ->random()
# ->randint()
# ->randrange()
# ->uniform()
# ->choice()

# ->random():
# ========
# It is a predefine function in python while working with random_module.The
# main objective of random_module is to generate the  random_values from 0.0 to 1.1

# from random import*
# print("=======using Random()=======")
# for x1 in range(10):
#     print(random())
# print()

# 0.0 to 1.1



# from random import*
# for x11 in range (11):
#     print(random())
# print() 

# randint():
# ===========
# it is a predefine function in python while working with random_module.the main objective tandint()
# function is generate the random_objects.it is mainly used to generate the otp,mobile_number.


# import time
# from random import*
# print("====one time pass word===")
# for x1 in range(10):
#     time.sleep(1)
#     print(randint(1,100000))
# print()

# from random import*
# print("=====one time password====")
# for x1 in range(10):
#     print(randint(9999,1000000))
# print()

# from random import*
# for x1 in range(10):
#     print(randint(2,120))
# print()

# from random import*
# for x2 in range(12):
#     print(randint(3,1225))
# print()



# --->>randrange():
# ==================
# it is a predefine function in python.the main objective of randrange() 
# function is to generate the random objects as per the application reqn...

#--->>randrange(begin,end(end-1),step)...

# from random import*
# print("====random_objects=====")
# for x1 in range(10):
#     print(randrange(15))
# print()


from random import*
for x1 in range(1):
    print(randint(1,6))
print()


# from random import*
# print("===random obects=====")
# for x1 in range(10):
#     print(randrange(5,15))
# print()


# from random import*
# print("====random_objects=====")
# for x1 in range(10):
#     print(randrange(5,15,1))
# print()


# from random import*
# for x1 in range(10):
#     print(randrange(0,10,1))
# print()
# for y1 in range(10):
#     print(randrange(1,10,2))
# print()


# uniform():
# ==========
# it is a predefine function in python.the main objective of uniform()
# function is to generate random values..

# from random import*
# print("====random_floating_point_numbers======")
# for x1 in range(10):
#     print(uniform(100,1000))
# print()

####....IT will give floating values upto 15numbers....

# choice():
# =========
# it is a predefine function in python.the main objective of choice() function
# is to perform random objects for string data type..


# from random import*
# print("======RANDOM_STRING_OBJECTS=======")
# s1=["a","b","c","d","e","f","g"]
# for x1 in range(7):
#     print(choice(s1))
# print()




