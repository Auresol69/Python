# nested loop = A loop within another loop (outer, inner)
#               outer loop:
#                   inner loop:

rows = int(input("Enter rows: "))
columns = int(input("Enter columns: "))
symbol = (input("Enter symbol: "))
for y in range(rows):
    for x in range(columns):
        print(symbol,end="")
    print()