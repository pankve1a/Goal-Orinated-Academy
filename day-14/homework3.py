# num1 = int(input("Enter the first integer: "))
# num2 = int(input("Enter the second integer: "))
# start = 0
# end = 0

# if num1 < num2:
#     end += num2
#     start += num1
# if num1 > num2:
#     end += num1
#     start += num2

# for i in range(start, end + 1):
#     if i % 5 == 0:
#         print(i)

list = []
num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))
for i in range(min(num1, num2), max(num1, num2)):
    list.append(i)
for num in list:
    if num % 5 == 0:
        print(num)