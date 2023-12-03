test = "Game 1: 1 green, 2 blue, 3 red; 5 red, 8 green, 7 blue"

for segments in test[test.find(": "):].replace(": ", "").split("; "):
    print(segments)