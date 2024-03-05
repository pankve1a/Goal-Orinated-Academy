# Ask user for two integer inputs
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Determine the lower and higher numbers
start = min(num1, num2)
end = max(num1, num2)

# Iterate using a for loop and print multiples of five
for i in range(start, end + 1):
    if i % 5 == 0:
        print(i)