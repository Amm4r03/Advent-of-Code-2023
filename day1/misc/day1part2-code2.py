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

sentence = "leightwoplxmgrcjcxrfqncvjfdvpgckmqfqsfqjthreefour2djnsvctlt"

# Define the size of the window
window_size = 5

# Iterate through the string with a window of size 5
for i in range(len(sentence) - window_size + 1):
    substring = sentence[i:i+window_size]
    for word, value in testing.items():
        substring = substring.replace(word, str(value))

