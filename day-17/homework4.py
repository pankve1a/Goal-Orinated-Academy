def find_largest_number(numbers):   
    max_num = numbers[0] 
    
    for num in numbers:
        if num > max_num:
            max_num = num
    
    return max_num

numbers = [10, 5, 20, 15, 8]
largest_num = find_largest_number(numbers)
print(f"The largest number in the list is: {largest_num}")
