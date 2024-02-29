authorise = False
password = "123"

while authorise != True:
    user_input = input("please enter your password: ")
    if user_input == password:
        print("accses granted")
        authorise = True
    elif user_input != password:
        print("wrong password, try again")

                    