def value():
    while True:
        money = input("输入兑换的金额，如12￥:")
        if money[-1] == "￥":
            dollor = str(int(money[0:-1])/6) +"$"
            break
        elif money[-1] == "$":
            dollor = str(int(money[0:-1])*6) +"￥"
            break
        else:
            print("输入“￥”或“$”为结尾")
    return dollor
print(value())
