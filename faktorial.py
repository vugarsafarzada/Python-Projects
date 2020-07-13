def factorials(num):
    i = 1
    z = 1
    while i<=num:
        z*=i
        i+=1
    print("Factorial: ",z)

usernum = int(input("Num: "))
factorials(usernum)

