# code for day 2 part 1

with open ("day2\\d2input.txt", "r") as f:
    fileText = f.read().splitlines()

gameSum = 0

for game in fileText:
    gameID = int(game[5:8].replace(":",""))       # 5th character in all lines is the game number
    
    gamePossible = True         # init game to be possible at first
    
    for segments in game[game.find(": "):].replace(": ", "").split("; "):
        gameCount = {}
        for segment in segments.split(", "):
            
            count, color = segment.split(" ")
            
            if color in gameCount.keys():
                gameCount[color] += int(count)
            else:
                gameCount[color] = int(count)
            
        # print(gameCount)
        if (gameCount.get('red', 0) > 12 or gameCount.get('green', 0) > 13 or gameCount.get('blue', 0) > 14):
            gamePossible = False
            print("game number {} NOT POSSIBLE".format(gameID))
            break
            
    if gamePossible:
        gameSum = gameSum + gameID
        print("game number {} is possible - adding to sum".format(gameID))

print("sum of possible game IDs : {}".format(gameSum))

# correct ans = 2076