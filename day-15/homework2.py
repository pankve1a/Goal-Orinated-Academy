password = "Goa_best"
entered_password = False
tries = 0

while entered_password != True:
    x = input("please enter your password: ")
    if x == "Goa_best":
        print("the password is correct.")
        break
    else:
        print("password is incorrect, try again.")
        tries += 1 
print(f"ot took you {tries} tries to enter your password.")

