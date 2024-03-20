def sum_and_len(numbers):
    if not numbers:
        return 0
    return sum(numbers), len(numbers) 
    

numbers = [1, 2, 3, 4, 5]
print(sum_and_len(numbers))