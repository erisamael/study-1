import numpy
def prime_iter(num):
    if num <= 1:
        return False
    for i in range(2,int(numpy.sqrt(num))+1):
        if num % i == 0:
            return False
    return True    #节约算力，虽然引进新库可能增加
def prime_range(n =100):
    for i in range(1,n+1):
        if prime_iter(i):
            print(i,end = " ")
#这边可能用个类也比较好hhh
prime_range()
