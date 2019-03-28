def output_dict
    list_e = [chr(i) for i in range(97,123)]#小写字母列表
    list_E = [chr(i) for i in range(65,91)] #大写字母列表,(黑魔法啊)
    dict = {}
    for i in range(0,26):
        dict[list_e[i]] = i+1
        dict[list_E[i]] = i+1
        i += 1

