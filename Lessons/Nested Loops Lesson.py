#Nested Loop Exercise - Square Drawing 6/3
#nested loop = a loop within a loop (outer, inner)

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range (rows):
    for y in range (columns):
        print(symbol, end ="")
    print("")