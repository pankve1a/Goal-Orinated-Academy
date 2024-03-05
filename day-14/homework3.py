num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# start = min(num1, num2)
# end = max(num1, num2)

start = 0
end = 0
if num1 < num2:
    end += num2
    start += num1
if num1 > num2:
    end += num1
    start += num2

# print(start)
# print(end)

for i in range(start, end + 1):
    if i % 5 == 0:
        print(i)