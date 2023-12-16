# code for day 4 part 1

with open ("day4\\input-test.txt", 'r') as file:
    text = file.read().splitlines()
    
totalSum = 0

for card in text:
    cardNum = card[5:8]
    segments = card[9::].split(" | ")
    winning = segments[0].split(" ")
    current = segments[1].split(" ")
    CurrentNums = [x for x in current if x != ""]
    winningNums = [x for x in winning if x != ""]
    
    matches = 0
    for key in winningNums:
        if key in CurrentNums:
            matches += 1
            # print("{} found in card {}\n".format(key, cardNum))
    if matches > 0:
        value = 2**(matches - 1)
    else:
        value = 0
    
    totalSum += value
    print(("card {} : {} points ({} matches)").format(cardNum, value, matches))

print("\n")
print(totalSum)
    
    # print("card number {}\nwinning card : {}\ncurrent numbers : {}\n".format(cardNum, winningNums, CurrentNums))