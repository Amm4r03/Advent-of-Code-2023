# code for day3 part 1

with open ("day3\\input-test.txt", 'r') as file:
    engineSchematic = file.read().splitlines()

def readNumber(engineSchematic, row, column):
    numberstr =""
    while column < len(engineSchematic[row]) and engineSchematic[row][column].isdigit():
        checkNearby(engineSchematic, row, column)
        numberstr += engineSchematic[row][column]
        column += 1
    return int(numberstr), column

def checkNearby(engineSchematic, row, column):
    while column < len(engineSchematic[row]) and engineSchematic[row][column].isdigit():
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= row + i < len(engineSchematic) and 0 <= column + j < len(engineSchematic[row]):
                    print(
                        "Neighboring characters of {} at ({}, {}) = {}".format(
                            engineSchematic[row][column],
                            row + i,
                            column + j,
                            engineSchematic[row + i][column + j]
                        )
                    )
        row += 1
        column += 1

special = ['+', '-', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

totalSum = 0

for column, line in enumerate(engineSchematic):
    row = 0
    while row < len(line):
        if line[row].isdigit():
            currentNum, row = readNumber(engineSchematic, column, row)
            print(currentNum, end=" ")
        else:
            row += 1
    print("")
    
checkNearby(engineSchematic, 0, 0)