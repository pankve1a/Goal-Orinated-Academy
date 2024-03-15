def strings_starting_with_a(input_list):
    result = []
    
    for string in input_list:
        if string.lower().startswith("a"):
            result.append(string)

    return result

input_list = ["asadas", "bdsadasd", "adsafadsf", "fdsafdfasasdf", "adasfasdf"]
result_list = strings_starting_with_a(input_list)
print(result_list)  
