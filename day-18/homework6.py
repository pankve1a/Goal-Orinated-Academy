def remove_duplicates(numbers):
    return list(set(numbers))

numbers = [1, 2, 3, 4, 2, 3, 5, 6, 7, 1]
filtered_numbers = remove_duplicates(numbers)
print(filtered_numbers)
