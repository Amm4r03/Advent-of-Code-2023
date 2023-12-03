# code for day 2 part 1

totalAvailable = {
    'red' : 12,
    'green' : 13,
    'blue' : 14
}

redCount = blueCount = greenCount = 0

with open("day2\\d2input-test.txt", "r") as file:
    lines = file.read().splitlines()

gamesum = 0

for line in lines:
    gamePossible = True
    gameNum = line[5]
    print("game number : {}\n".format(gameNum))
    segments = line[line.index(":")+2:].split("; ")
  
    gameCount = {} 
  
    for segment in segments:
        print(segment)
        cubes = segment.split(", ")
        for cube in cubes:
            count, color = cube.split()

            if color in gameCount:
                gameCount[color] += int(count)
            else:
                gameCount[color] = int(count)
    
        redCount = gameCount.get('red', 0)
        blueCount = gameCount.get('blue', 0)
        greenCount = gameCount.get('green', 0)
        
        if redCount > 12 or greenCount > 13 or blueCount > 14:
            gamePossible = False
        
    if gamePossible:
        gamesum = gamesum + int(gameNum)

print(gamesum)