# testing code for day 1

NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

sen = "hellomy4amm6rn5me"

digitSen = ''

for i in sen:
    if i in NUMBERS:
        digitSen = digitSen + i


print(int(digitSen[0]) * 10 + int(digitSen[-1]))