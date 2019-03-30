import numpy
def prime_iter(num):#做了重复功，正在学习os和sys导入解压文件夹为库，本地操作，不过有点困难就是了，之后直接导入前面的函数是最好的
    num = int(num)
    if num <= 1:
        return False
    for i in range(2,int(numpy.sqrt(num))+1):
        if num % i == 0:
            return False
    return True
while True:
    N = input("输入要判断的正整数：(不输入退出)")
    if N == "":
        break
    elif int(prime_iter(N)) == True:
        print("该数为质数")
    elif int(prime_iter(N)) == False:
        print("该数为合数")
