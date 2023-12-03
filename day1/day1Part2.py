# attempt 2 at day1part2 prompt

# new approach : make use of 'o1e', 't2o' sets for cases such as 'oneight'
# 'oneight' should give 18 according to case

NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

numReplacements = {
    'one' : 'o1e',
    'two' : 't2o',
    'three' : 't3e',
    'four' : 'f4r',
    'five' : 'f5e',
    'six' : 's6x',
    'seven' : 's7n',
    'eight' : 'e8t',
    'nine' : 'n9e',
    'zero' : 'z0o'
}

frequencies = {}
sum = 0

with open("C:\\Users\\ahmad\\Desktop\\Ammar\\College\\code\\Advent of Code 2023\\day1\\CalibrationDocument.txt", "r") as file:
    for line in file:
        for word, number in numReplacements.items():
            index = line.find(word)
            if index != -1:
                frequencies[word] = index
        sortedDict = sorted(frequencies.items(), key = lambda x : x[1])
        
        newsen = line
        
        for item in sortedDict:
            word = item[0]
            value = numReplacements[word]
            newsen = newsen.replace(word, str(value))
        
        numlist = []
        for char in newsen: 
            if char in NUMBERS:
                numlist.append(char)
        number = str(numlist[0]) + str(numlist[-1])
        number = int(number)
        
        sum += number

print(sum)