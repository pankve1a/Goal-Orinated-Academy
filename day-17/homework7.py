def sum_numbers_greater_than_10(input_list):
    total = 0
    
    for number in input_list:
        if number > 10:
            total += number
    
    return total

input_list = [4324242, 11, 6, 43, 10]
result = sum_numbers_greater_than_10(input_list)
print(result) 
