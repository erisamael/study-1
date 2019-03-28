def output_dict(): #创建一个字典
    list_e = [chr(i) for i in range(97,123)]#小写字母列表
    list_E = [chr(i) for i in range(65,91)] #大写字母列表,(黑魔法啊)
    dict1 = {}
    for i in range(0,26):
        dict1[list_e[i]] = (i+1)
        dict1[list_E[i]] = (i+1)
        i += 1
    return dict1
dict2 = output_dict()
name = input("输入名字：")
sun = 0
for m in range(len(name)):
    sun += int(dict2.get(name[m]))
print(sun)
