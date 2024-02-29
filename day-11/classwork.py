password = "123"
logged_in = False

while logged_in != True:
    guess = input("please enter the password: ")

    if guess == password:
        print("accses granted")
        logged_in = True
    else:
        print("try again")