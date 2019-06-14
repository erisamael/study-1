dict_f = {}
fileon = open("test.txt","r")
str_file = fileon.read()
for i in str_file:
    if i in [" ",",",".","?","!"]:
        continue
    elif i not in dict_f:
        dict_f[i] = 1
    else:
        dict_f[i] +=1
print(dict_f)
fileon.close()
