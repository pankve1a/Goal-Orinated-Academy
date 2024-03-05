authorized = False
password = "abc123"

while authorized != True:
    login = input("please enter your password: ")
    if login == password:
        print("acccess granted")
        break
    
        