# 1)
number1 = int(input("please enter the first number: "))
number2 = int(input("please enter the second number: "))

for i in range(number1, number2 + 1):
    print(i)

# 2)
number1 = int(input("please enter the first number: "))
number2 = int(input("please enter the second number: "))
total = 0
for i in range(number1, number2 + 1):
    total += i
print(total)

# 3)
number1 = int(input("please enter the first number: "))
number2 = int(input("please enter the second number: "))
for i in range(number1, number2 + 1):
    square = i ** 2
    print(square)