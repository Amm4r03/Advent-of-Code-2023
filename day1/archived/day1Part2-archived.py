# part 2 code

NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

WORDS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero']

numWords = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9,
    "zero" : 0 
}

frequencies = {}
sum = 0

with open("C:\\Users\\ahmad\\Desktop\\Ammar\\College\\code\\Advent of Code 2023\\day1\\CalibrationDocument-test.txt", "r") as file:
    for line in file:
        for word, number in numWords.items():
            index = line.find(word)
            if index != -1:
                frequencies[word] = index
        sortedDict = sorted(frequencies.items(), key = lambda x : x[1])
        
        newsen = line
        
        for item in sortedDict:
            word = item[0]
            value = numWords[word]
            newsen = newsen.replace(word, str(value))
        # till now we have converted all relevant characters to the number (string format)
        # we can now employ the method used in part 1 to get the numbers for each line
        
        numList = []
        for char in newsen:
            if char in NUMBERS:
                numList.append(char)
        number = str(numList[0]) + str(numList[-1])
        number = int(number)
        
        sum += number
            
print(sum)
# expected val : 281
# actual answer : 