num = int(input("Enter the number of rows: "))
for row in range(num):
    val = row + 1
    dec = num - 1
    for col in range(row + 1):
        print(format(val, "<4"), end=" ")
        val = val + dec
        dec = dec - 1
    print()