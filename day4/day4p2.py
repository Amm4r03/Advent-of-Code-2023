# code for day 4 part 2

with open ("day4\\input-test.txt", 'r') as file:
    text = file.read().splitlines()

matches = 0

cardCopies ={}
cardCount = {} 

for i, card in enumerate(text):
    cardNum = (int)(card[5:8].replace(":",""))
    segments = card[9::].split(" | ")
    winning = segments[0].split(" ")
    current = segments[1].split(" ")
    CurrentNums = [x for x in current if x != ""]
    winningNums = [x for x in winning if x != ""]
    
    # print("card {}\nwinning numbers : {}\ncurrent numbers : {}".format(cardNum, winningNums, CurrentNums))
    
    cardCount[cardNum + i + 1] = 1
    
    for key in winningNums:
        if key in CurrentNums:
            matches += 1
    print(("card {} : {} matches\ncards numbers won : ").format(cardNum, matches), end = " ")
    for i in range(matches):
        print("{}".format(cardNum + i + 1),end = " ")
        if (cardNum + i + 1) in cardCopies:
            cardCopies[cardNum + i + 1] += 1
        else:
            cardCopies[cardNum + i + 1] = 1
        
    # for j in range(cardCopies.get(cardNum + i + 1, 0)):
    #     print("okok {}".format(j))
            
            
    print("\n\n")
    matches = 0

print(cardCopies)
print("total copies : {}".format(sum(cardCopies.values())))

# will check later
# notes :
# current line only decides future lines, can calculate iteratively
# count number of copies of card
# count matches of card, multiply with copies
# return to dictionary, move to next card