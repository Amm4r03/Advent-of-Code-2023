sum = 0

NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

with open("C:\\Users\\ahmad\\Desktop\\Ammar\\College\\code\\Advent of Code 2023\\day1\\CalibrationDocument-test.txt", "r") as file:
    for line in file:
        digitSen = ''
        for char in line:
            if char in NUMBERS:
                digitSen = digitSen + char
        if (digitSen):
            lineSum = int(digitSen[0]) * 10 + int(digitSen[-1])
            sum = lineSum + sum

print(sum)

# ans = 56108