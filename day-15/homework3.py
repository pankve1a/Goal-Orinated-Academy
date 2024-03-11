string_input = input("please enter a string: ")

while string_input[0] != "G":
 
    if len(string_input) == 0:
        print("thats not a word")
    elif string_input[0] == "G":
        print("thats true")
        break
    else:
        print("the word doesnt have G in it")
        

