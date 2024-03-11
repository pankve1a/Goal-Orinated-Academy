# list = []
# for i in range(0, 50):
#     list.append(i)

# print(list[:25 + 1])
# print(list[::3])

start = int(input("Enter number: "))
end = start + 10
new_list = []

for i in range(start, end + 1):
    new_list.append(i)

print(new_list)
print(new_list[::2])
