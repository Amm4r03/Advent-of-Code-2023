with open ("day3\\input.txt", 'r') as file:
    schematic = file.read().splitlines()
    
with open("day3\\input-processing-2.txt", 'w') as writeFile:
    for line in schematic:
        writeFile.write(line.replace(".", " ") + '\n')
    print("written to file")