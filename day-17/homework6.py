def square_numbers(input_list):
    result = []
    
    for number in input_list:
        result.append(number ** 2)
    
    return result

input_list = [5, 2, 76, 454543535, 1]
result_list = square_numbers(input_list)
print(result_list)  
