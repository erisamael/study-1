afileon = open("A.txt","r")
bfileon = open("B.txt","r")
str_f = afileon.read()
num_f = bfileon.read()
dict_f = {}
for i in range(len(num_f)):
	dict_f[str_f] = eval(num_f)
print(dict_f)
