number = input("please select your number:")
number = int(number)
def collatz(number):
    if number %2 == 0:
        number = number // 2
    elif number %2 == 1:
        number = number*3+1
    return number
while number != 1:
    number = collatz(number)
    print(number)
    if number == 1:
        break
print("over")
    
    
