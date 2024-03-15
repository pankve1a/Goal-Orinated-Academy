def finding_even(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = finding_even(numbers)
print("Even numbers in the list:", even_numbers)
