# user input = number of rows
rows = int(input("Enter the number of rows: "))
# starting number
number = 1
# loop through each row with for loop, increasing by 1 till it reaches the user input
for i in range(1, rows + 1):
    # numbers in each row, increasing by 1
    for r in range(1, i + 1):
        print(number, end=" ")
        number += 1
#next row // space
    print()  