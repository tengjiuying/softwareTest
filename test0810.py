"""
a = 1
print(a)
#id可以打印变量存储地址
print(id(a))
"""

# print = 1
# x=3
# if x>2:
#     print("xixi")
# else:
#     print("lala")
import random

com_num = random.randint(1,100)
print(com_num)
while True:
    per_num = int(input("请输入一个数字："))
    if per_num > com_num:
        print("小一点")
    elif per_num < com_num:
        print("大一点")
    else:
        print("猜对了")
        break