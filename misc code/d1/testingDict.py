# testing part 2 code

NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

WORDS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero']

testing = {
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

sentence = "h3lloeightwoseven"

for word, value in testing.items():
    sentence = sentence.replace(word, str(value))
    
print(sentence)