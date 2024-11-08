# nested loops=loops within another loop(outer,inner):
                # outer loop:
                #     inner loop:

rows= int(input("enter the # of rows"))
columns= int(input("enter the # of columns"))
symbol =input("enter a symbol to use: ")


for x in range(rows):
    for y in range(columns):#ten is exclusive,1 is inclusive
        print(symbol, end="")#in between each letter
    print()


for x in range(3):
    for y in range(1,10):#ten is exclusive,1 is inclusive
        print(y, end ="/")#in between each letter

    print()
