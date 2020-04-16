def count_char_freq(str):
    new_str = {}
    for char in str:
        if char in new_str:
            new_str[char] += 1
        else:
            new_str[char] = 1
    print(new_str)
        
count_char_freq("google.com")