def strtodictlist(x,dict = True):
  list_s = x.split("|")
  list_d = []
  list_t = []
  for i in list_s:
    list_d.append(i.split(":"))
    list_t.append(tuple(i.split(":")))
   dict_x = dict(list_d)
   if dict = True:
    return dict_x
   else:
    return list_t
