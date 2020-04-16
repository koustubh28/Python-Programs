def modify_string(str):
    length_of_string = len(str)
    if length_of_string < 2:
        return "Invalid string"
    else:
        return str[0:2] + str[(length_of_string)-2:length_of_string]

result = modify_string("c")
print(result)