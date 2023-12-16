with open("day6\\input.txt", 'r') as file:
    text = file.read().splitlines()

timeString = text[0][13:].split("   ")
distanceString = text[1][11:].split("   ")

times = [int(x) for x in timeString]
distances = [int(x) for x in distanceString]

finalProd = 1

for allowedTime, distanceRecord in zip(times, distances):
    recordBroken = sum(1 for j in range(allowedTime) if j * (allowedTime - j) > distanceRecord)
    finalProd *= recordBroken

print(finalProd)