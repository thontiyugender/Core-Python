# ->frozenset:
# ============
# Python supports frozenset data type.It is exactly same as set data type.Where
# Set data type is mutable object and frozenset data type is immutable object.


# Ex1:
# ====
# import time 
# S1={1001,1002,1003,1004,1005,1006}
# S2=frozenset(S1)
# print(S2)
# print()
# print(type(S2))
# print()
# time.sleep(2)
# print('End of an application')


# Interview_Question:
# ==================
# Q1)What is difference between Tuple data type and Frozenset data type?

# Both are immutable objects meant for readability operations


# # Ex1:
# # ===
import time 
T1=(10001,1002,1003,1004,1005,1006,1001,1002,1003)
print(T1)
print()
print(type(T1))
print()
S1={10001,1002,1003,1004,1005,1006,1001,1002,1003}
S2=frozenset(S1)
print(S2)
print()
print(type(S2))
print()
time.sleep(2)
print('End of an application')


# import time 
# S1={1001,1002,1003,1004,1005,1006}
# S2=frozenset(S1)
# print(S2)
# print()
# print(type(S2))
# print()
# time.sleep(2)
# print('End of an application')

# import time
# S1={1212,12,1,2,2154544,4,46465,4444,44844,448,4,8484,4,44,444,44,4,4,4}
# S2=frozenset(S1)
# print(S2)
# print()
# print(type(S2))
# print(type(S1))
# print()
# time.sleep(1)
# print("End of an application")


import time
T1=(12,5,15,51,5,55,55,5,55,5,6)
print()
print(T1)
print()
print(type(T1))
print()
S1={12,5,15,51,5,55,55,5,55,5,6}
S2=frozenset(S1)
print()
print(S1)
print()
print(type(S1))
print()
time.sleep(1)
print("End of an application")