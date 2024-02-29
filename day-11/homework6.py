age = int(input("Enter your age: "))

if age < 0:
    print("this age doesnt exist")
elif age < 13:
    print("you are a child")
elif age < 20:
    print("you are a teenager")
else:    
    print("you are an adult")