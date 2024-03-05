my_array = []

for i in range(50, 101):
    my_array.append(i)

print("Array with negative indexes:")
for i in range(-1, -len(my_array)-1, -1):
    print(my_array[i])