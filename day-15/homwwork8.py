name = input("Please enter your name: ")
if len(name) > 0: 
    last_letter = name[-1] 
    print(f"The last character of your name is: {last_letter}")
else:
    print("You didn't enter any name.")
