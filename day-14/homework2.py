# Create an empty array
my_array = []

# Add numbers from 50 to 100 to the array
for i in range(50, 101):
    my_array.append(i)

# Print the part of the array with negative indexes
print("Array with negative indexes:")
for i in range(-1, -len(my_array)-1, -1):
    print(my_array[i])