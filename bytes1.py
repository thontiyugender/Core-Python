# # Bytes data type:
# # ===============
# # Python supports Bytes data type.The main objective of Bytes data type is work
# # on audio,video,semi structure files(XML/JSON).Bytes data type is immutable object.While working with bytes data types the range must be from 0-256-1=255.
# #                                                                                                                                              =============


# # import time
# # L1=[1,25,26,28464,145,1515,14]
# # res1=bytes(L1)
# # print()
# # print(res1)
# # print()
# # print(type(res1))
# # print()
# # time.sleep((2))
# # print("End of an application")


# # Ex1:
# # ===
# # import time 
# # L1=[121,122,134,156,167,189,1200]
# # res1=bytes(L1)
# # print(res1)
# # print()
# # print(type(res1))
# # print()
# # time.sleep(2)
# # print('End of an application')


# # # OUTPUT:
# # # ======

# # # C:\Users\Admin\Desktop>Python test1.py
# # # Traceback (most recent call last):
# # #   File "test1.py", line 3, in <module>
# # #     res1=bytes(L1)
# # # ValueError: bytes must be in range(0, 256)


# # import time
# # L1=[1,52,65,12,58,95]
# # res1=bytes(L1)
# # print()
# # print(res1)
# # print()
# # print(type(res1))
# # print()
# # time.sleep(2)
# # print("end of an application")


# # # Ex2:
# # # ===
# # import time 
# # L1=[121,122,134,156,167,189,255]
# # res1=bytes(L1)
# # print(res1)
# # print()
# # print(type(res1))
# # print()
# # time.sleep(2)
# # print('End of an application')


# # # Ex3:
# # # ====
# # import time 
# # L1=[121,122,134,156,167,189,255]
# # res1=bytes(L1)
# # print(res1)
# # print()
# # print(*res1)                                # IF WE USE * THEN WE GET VALUES OF BYTES.......
# # print()
# # print(type(res1))
# # print()
# # time.sleep(2)
# # print('End of an application')

# # Ex4:
# # ====
# # import time 
# # L1=[121,122,134,156,167,189,255]
# # res1=bytes(L1)
# # print(res1)
# # print()
# # for x1 in res1:
# #     print(x1)
# # print()
# # print(type(res1))
# # print()
# # time.sleep(2)
# # print('End of an application')

# import time
# L1=[121,12,55,58,99,89,54,55]
# res1=bytes(L1)
# print()
# print(res1)
# for x1 in res1:
#     print(x1)
# print()
# print(x1)
# print()
# time.sleep(2)
# print("End of an application")

# # import time
# # l1=[12,5,58,69,47,55,68]
# # print("===before mutable operations====")
# # res1=bytes(l1)
# # print()
# # print(res1)
# # print(*res1)
# # print()
# # print(type(l1))
# # print("===after mutable operations===")
# # res1[0]=25
# # res1[1]=65
# # res1[2]=66
# # print()
# # print(res1)
# # print(*res1)
# # time.sleep(1)
# # print("End of an application")


# # Ex5:
# # ====
# # import time 
# # L1=[121,122,134,156,167,189,255]
# # print("====Before mutable operations====")
# # res1=bytes(L1)
# # print()
# # print(res1)
# # print()
# # print(*res1)
# # print()
# # print("====After mutable operations====")
# # res1[0]=111
# # res1[1]=112 
# # res1[2]=113 
# # res1[3]=114
# # print(res1)
# # print()
# # print(*res1)
# # print()
# # time.sleep(2)
# # print('End of an application')

# import time 
# L1=[121,122,134,156,167,189,255]
# print("====Before mutable operations====")
# res1=bytes(L1)
# print()
# print(res1)
# print()
# print(*res1)
# print("===indexing===")
# print()
# print(res1[0])
# print(res1[1])
# print(res1[2])
# print()
# print("===slicing===")
# print(res1[1:])
# print(*res1[1:])
# print(*res1)
# print()
# time.sleep(2)
# print("End of an application")


# # ->bytearray data type:
# # =====================
# # Python supports bytearray data type.The main objective of bytearray is to work on audio,video,semi structure files(JSON/XML).bytearray is a mutable object.

# import time
# l1=[1,2,3,8,94,97,97,7,4,4,6,5,45,9,94,98,9,97,97,98,47,78,7,99,124,58]
# res1=bytearray(l1)
# print()
# print(res1)
# print()
# print(*res1)
# time.sleep(1)
# print("End of an application")

# import time
# Lambda=[1,52,68,125,254,125,132]
# res1=bytearray(Lambda)
# print()
# print(res1)
# print()
# print(*res1)
# print(type(res1))
# print()
# time.sleep(2)
# print("End of an applcation")

# # Ex1:
# # ===
# import time 
# L1=[121,122,134,156,167,189,256]
# res3=bytearray(L1)
# print(res3)
# print()
# print(type(res3))
# print()
# time.sleep(2)
# print('End of an application')


# # Ex2:
# # ===
# import time 
# L1=[121,122,134,156,167,189,255]
# res3=bytearray(L1)
# print(res3)
# print()
# print(type(res3))
# print()
# time.sleep(2)
# print('End of an application')

import time
l1=[52,252,235,22,232,24,254,251,252]
res=bytearray(l1)
print()
print(res)
print(type(res))
print(*res)
print()
time.sleep(1)
print("End of an application")

# import time
# l1=[12,52,56,57,86,215,98]
# res2=bytearray(l1)
# print()
# print(res2)
# print()
# print(*res2)
# print()
# for y1 in res2:
#     print(y1)
# print()
# print(type(res2))
# print()
# time.sleep(2)
# print("end of an application")

# # Ex4:
# # # ====
# import time 
# L1=[121,122,134,156,167,189,255]
# res3=bytearray(L1)
# print(res3)
# print()
# for y1 in res3:
#     print(y1)
# print()
# print(type(res3))
# print()
# time.sleep(2)
# print('End of an application')


# Ex5:
# ====
# import time 
# L1=[121,122,134,156,167,189,255]
# print("====Before mutable operations====")
# res4=bytearray(L1)
# print(res4)
# print()
# print(*res4)
# print()
# print(type(res4))
# print("====After mutable operation====")
# res4[0]=1 
# res4[1]=2
# res4[2]=3 
# res4[3]=4 
# res4[4]=5 
# res4[5]=6
# res4[6]=7 
# print(res4)
# print()
# print(*res4)
# print()
# print(type(res4))
# print()
# time.sleep(2)
# print("End of an application")

# import time
# l1=[1,44,58,96,54,55,86,35,125,185]
# res4=bytearray(l1)
# print()
# print(res4)
# print(*res4)
# print()
# print(type(l1))
# print("====INDEXING=====")
# print()
# print(res4[0])
# print(res4[1])
# print(res4[3])
# print(res4[4])
# print(res4[5])
# print(res4[6])
# print(res4[7])
# print(res4[8])
# print(res4[9])
# print()
# print(type(l1))
# print(l1)
# time.sleep(1)
# print("End of an application")

# import time
# L1=[21,125,132,162,184,59,159,251,165]
# res1=bytearray(L1)
# print(res1)
# print(*res1)
# print()
# print("====mutable operation====")
# print()
# res1[0]=112
# res1[1]=56
# res1[2]=25
# print()
# print(res1)
# print(*res1)
# print(L1)
# print()
# time.sleep(1)
# print("End of an application")