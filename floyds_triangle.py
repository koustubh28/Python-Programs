input_value = int(input("Enter the number of rows:"))
num = 1
for row in range(1, input_value+1):
    for col in range(1, row+1):
        print(num, end=" ")
        num = num + 1
    print()