# new approach for d1p2 code

# sentence = "meightwodccsxmc4nvq3sevenqdshf"

'''
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
'''

sentence = "two1nine"

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

for word, number in numWords.items():
    index = sentence.find(word)
    if index != -1:
        frequencies[word] = index

sortedDict = sorted(frequencies.items(), key= lambda x:x[1])

newsen = sentence

for item in sortedDict:
    
    word = item[0]
    index = item[1]
    value = numWords[word]
    
    newsen = newsen.replace(word, str(value))

print(newsen)

