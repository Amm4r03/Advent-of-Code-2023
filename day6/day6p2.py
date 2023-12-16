# code for day 6 part 2

with open("day6\\input.txt", 'r') as file:
    text = file.read().splitlines()

times = text[0][13::]
time = (int)("".join(times.split()))

distances = text[1][11::].split()
distance = (int)("".join(distances))

recordBroken = 0

for i in range(time):
    distanceCovered = i * (time - i)
    if distanceCovered > distance:
        recordBroken += 1
        
print(recordBroken)

# answer = 34123437