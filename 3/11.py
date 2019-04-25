for i in range(1,10001):
    str_i = str(i)
    sum_i = 0
    for m in range(len(str_i)):
        sum_i +=  pow(int(str_i[m]) , len(str_i))
    if sum_i == i:
        print(i)
