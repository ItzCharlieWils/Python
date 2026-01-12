#loop within another loop

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
symbols = input("Enter symbols to use: ")
for i in range(rows):
    for j in range(columns):
        print(symbols, end="")
    print()