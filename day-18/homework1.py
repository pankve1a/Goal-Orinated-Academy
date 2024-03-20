def filter_fours():
    numbers = []
    filtered_numbers = []

    for i in range(1, 20 + 1):
        numbers.append(i)

    print(numbers)

    for i in numbers:
        if i % 4 == 0:
            filtered_numbers.append(i)
        return filtered_numbers

result_list = filter_fours()
print(result_list)
