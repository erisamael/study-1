#字符串切片法
import random
i = 0
while i == 0:
     num = random.randint(10000,99999)
     num_str = str(num)
     if int(num_str[0]) >2 and int(num_str[0]) <8:
          if int(num_str[1]) > 5:
               if int(num_str[2]) < 4:
                    if int(num_str[3]) > int(num_str[4]):
                         print(num)
                         break
     
#其他方法
import re

