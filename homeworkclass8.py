N = input("请输入这个正整数：")
sun,tem = 0,0
for i in range(len(N)):
    tem = int(N[i]) * int(N[i])
    sun+=tem
print(sun)
