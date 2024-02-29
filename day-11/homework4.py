balance = 1000
pin = 1234
x = int(input("welocome, please enter your pin: "))
if x == pin:
    print("the pin is correct")
    y = input("do you wish to withdraw money or check balance? ")
    if y.lower() == "check balance":
        print("your balance is " + str(balance) + " dollars")
    elif y.lower() == "withdraw money":
        z = input("p`lease enter how much money you want to withdraw: ")
        print("you withdrew " + str(z) + " dollars")
else:
    quit()