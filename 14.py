inventory = {}
def inventory_write():
    while True :
        obj = input ("please input your object(blank to exit): ")
        num = int(input ("please input your object's number: "))
        inventory[obj] = num
        if obj == "" :
            break
        return inventory
def display_inventory(inventorys):
    item_total = 0
    print("Inventory:")
    for k, v in inventorys.items():
        print(str(v) + " " +k)
        item_total += int(v)
    print("total number if items:" + str(item_total))
#
import pprint
while 1=1 :
    bag = open('bag.txt','r')
    inventory = eval(bag.read())
    if inventory  == "":
        inventory = {}
    bag.close()
    ans3 = input("请选择您想做的：1.查看背包   2.放入物品至背包   3.退出（填入数字）: ")
    if ans3 == "2":
        inventory_write()
    if ans3 == "1" :
        display_inventory(inventory)
    if ans3 == "3" :
        bag = open ('bag.txt','w')
        inventory_str = pprint.pformat(inventory)
        bag.write(inventory_str)
        bag.close()
        break
