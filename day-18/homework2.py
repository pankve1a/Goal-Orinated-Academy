# def even_indexes(lastname):
#     char_list = []
    
#     for char in lastname:
#         char_list.append(char)

#     print(char_list)

 
# lastname = input("please enter lastname: ")
# even_indexes(lastname)


# def even_indexes(lastname):
#     result = ''

#     for index in range(len(lastname)):
#         if index % 2 == 0:
#             result = result + lastname[index]
    
#     return result


# lastname = input("Please enter lastname: ")

# print(even_indexes(lastname))
def filter_arr(first_name, last_name):
    user_list = []
    filter_arr.append((first_name, last_name))
    return user_list

first_name = input("enter your first name: ")
last_name = input("enter your last name: ")

user_list = filter_arr(first_name, last_name)

print(user_list)