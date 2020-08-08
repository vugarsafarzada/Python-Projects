s_uname = "vuqarsefer"
s_upasw = "2001"

print('username: {},\n password: {}'.format(s_uname,s_upsaw))

mistake = 3

while True:
    print()
    print("You can make",mistake,"times mistake!")
    usname = input("User name: ")
    uspasw = input("User password: ")
    
    if (s_uname == usname and s_upasw != uspasw):
        print()
        print("Password invalid")
        mistake -=1
        
    elif (s_uname != usname and s_upasw == uspasw):
        print()
        print("Username invalid")
        mistake -=1
    elif (s_uname != usname and s_upasw != uspasw):
        print()
        print("Username and Password invalid!")
        mistake -=1
    else:
        print()
        print("Login successful!")
        break
    if(mistake == 0):
        print("Giris hakki son!")
        break
    
