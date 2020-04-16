def calculate_string_len(words):
    counter = 0
    word = ""
    for letter in words:
        word += letter
        counter = counter + 1
    return 'The length of the', word, 'is', counter

result = calculate_string_len("koustubh")
print(result)