num = int(input("enter number for factorial"))
# temp = 1
# for i in range(num):
#     temp = temp * num
#     num -= 1
# print(str(temp))


#range three parameters type
temp2 = 1
for i in range(num, 0, -1):
    temp2 *= i
print(str(temp2))
