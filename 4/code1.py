dict_f = {}
file = open("test.txt","r")
str_file = file.read()
for i in str_file:
  if i in [" ",",",".","?","!"]:
    continue
   elif i in dict_f:
    dict[i] += 1
   else:
    dict[i] = 1
