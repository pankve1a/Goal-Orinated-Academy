names_list = []

age = int(input("Please enter your age: "))
if age > 18:
    name = input("Please enter your name: ")
    names_list.append(name)
    print("Names list:", names_list)
else:
    print("your age is not valid.")

