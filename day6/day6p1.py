# code for day 6 part 1

with open("day6\\input.txt", 'r') as file:
    text = file.read().splitlines()

timeSliced = text[0][13::]
distanceSliced = text[1][11::]
timeString = timeSliced.split("   ")
distanceString = distanceSliced.split("   ")
times = [int(x) for x in timeString]
distances = [int(x) for x in distanceString]

finalProd = 1
    
for i in range(len(times)):
    recordBroken = 0
    # print("race {} : {} m |  {} s".format(i+1, times[i], distances[i]))
    distanceRecord = distances[i]
    allowedTime = times[i]
    
    for j in range(allowedTime):
        distanceCovered = j * (allowedTime - j)
        if distanceCovered > distanceRecord:
            recordBroken += 1
        # print(distanceCovered)
    finalProd = recordBroken * finalProd

print(finalProd)

# answer = 131376