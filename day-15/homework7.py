x = int(input("Please enter the first number: "))
y = int(input("Please enter the second number: "))
z = input("Enter an operator: ")

if z == '+':
    result = x + y
    print(f"the result is {result}")
elif z == '-':
    result = x - y
    print(f"the result is {result}")
elif z == '/':
    result = x / y
    print(f"the result is {result}")
elif z == '*':
    result = x * y
    print(f"the result is {result}")
elif z == '**':
    result = x ** y
    print(f"the result is {result}")
else:
    print("Invalid operator. quiting.")
