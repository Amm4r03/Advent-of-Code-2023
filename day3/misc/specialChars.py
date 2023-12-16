with open ("day3\\input-test.txt", 'r') as file:
    schematic = file.read().splitlines()
    
special = ['+', '-', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

for column, line in enumerate(schematic):
    for row, char in enumerate(line):
        if char in special:
            
            print("[found {} at ({}, {})]".format(char, row, column))
            
def checkNearbyNumbers(schematic, row, column):
    pass