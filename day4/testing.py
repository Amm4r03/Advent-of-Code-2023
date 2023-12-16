with open("day4\\input-test.txt", 'r') as file:
    text = file.read().splitlines()

cardCopies = {}

originalScratchcards = list(range(1, len(text) + 1))

while originalScratchcards:
    currentScratchcard = originalScratchcards.pop(0)
    count = cardCopies.get(currentScratchcard, 0)

    for i in range(count):
        originalScratchcards.append(currentScratchcard + i + 1)

    if currentScratchcard not in cardCopies:
        cardCopies[currentScratchcard] = 1
    else:
        cardCopies[currentScratchcard] += 1

totalScratchcards = len(originalScratchcards) + sum(cardCopies.values())
print(cardCopies)
print(f"Total scratchcards: {totalScratchcards}")