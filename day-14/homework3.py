num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

start = min(num1, num2)
end = max(num1, num2)

for i in range(start, end + 1):
    if i % 5 == 0:
        print(i)