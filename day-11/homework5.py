user = "admin"
password = "password123"
user_input1 = input("please enter your user: ")
user_input2 = input("please enter your password: ")
if user_input1 == user and user_input2 == password:
        print("Login successful")
else:
        print("Incorrect username or password")