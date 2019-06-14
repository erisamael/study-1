doublelist = eval(input("输入一个二维数组："))
for i in range(len(doublelist)):
    for m in range(i+1):
        print(doublelist[i][m],end = " ")
    print("")
