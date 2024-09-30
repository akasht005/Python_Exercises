num = int(input("Enter a number : "))

flag = False
if (num == 0 or num == 1):
    print("Not a prime")
elif num > 1:
    for i in range(2,num):
        if num % i == 0:
            flag = True
            break
    if flag:
       print("Not a prime")
    else:
        print("Prime")
            