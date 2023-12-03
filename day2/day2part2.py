# code for day 2 part 2

with open ("day2\\d2input.txt", "r") as f:
    fileText = f.read().splitlines()

powerSum = 0

for game in fileText:
    gameID = int(game[5:8].replace(":",""))       # accesses the game number
    
    reds = []
    blues = [] 
    greens = []
    
    for segments in game[game.find(": "):].replace(": ", "").split("; "):
        gameCount = {}
        for segment in segments.split(", "):
            
            count, color = segment.split(" ")
            
            if color in gameCount.keys():
                gameCount[color] += int(count)
            else:
                gameCount[color] = int(count)
        
        reds.append(gameCount.get('red', 0))
        reds.sort(reverse=True)
        
        blues.append(gameCount.get('blue', 0))
        blues.sort(reverse=True)
        
        greens.append(gameCount.get('green', 0))
        greens.sort(reverse=True)
    
    redMin = reds[0]
    greenMin = greens[0]
    blueMin = blues[0]
    
    gameProd = redMin * greenMin * blueMin
    
    powerSum += gameProd
    
    # print("Game {}\nred : {}\ngreen : {}\nblue : {}\nproduct = {}*{}*{} = {}".format(gameID, redMin, greenMin, blueMin, redMin, greenMin, blueMin, gameProd))
    # print("current total sum = {}".format(powerSum))
    
print(powerSum)