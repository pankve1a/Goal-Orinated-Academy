text = "Write a Write a function that takes a list of strings as input and  returns a new list containing only the strings that have a length greater than 5"
def strings_by_length(text):
    strings = text.split(" ")
    result = []
    for s in strings:
        if len(s) > 5:
            result.append(s)
    return " ".join(result)
print(strings_by_length(text))


