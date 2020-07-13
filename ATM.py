print("""
************************************
-- WELCOME TO SAFARZADA ATM --

           COMMANDS:

    (1) - LOOK AT MY BALANCE

    (2) - INCREASE BALANCE

    (3) - WITHDRAW MONEY

    (0) - EXIT

************************************
""")

balance = 1000
while True:
    print()
    cmd = int(input("COMMAND: "))
    print()
    
    if cmd == 1:
        print("---------------------")
        print("YOUR BALANCE: ")
        print(balance,"$")
        print("---------------------")

    elif cmd == 2:
        inc = int(input("ENTER YOUR MONEY PLEASE: "))
        balance += inc
        
        print("---------------------")
        print("PROCESS IS SUCCESSFUL")
        print("---------------------")

    elif cmd == 3:
        while True:
            hwmch = int(input("ENTER QUANTITY: "))
            if hwmch > balance:
                print("---------------------")
                print("ERROR!!!")
                print("INSUFFICIENT FUNDS, YOUR BALANCE:",balance,"$")
                print("---------------------")

            else:
                balance -= hwmch
                print("---------------------")
                print("PROCESS IS SUCCESSFUL")
                print("---------------------")
                break
    elif cmd == 0:
        print("---------------------")
        print("GOODBYE!")
        print("---------------------")
        break        
    else:
        print("---------------------")
        print("COMMAND IS NOT TRUE!")
        print("REPEAT PLEASE!")
        print("---------------------")












