# calculating time taken for computation - day 6 part 2

import time

# code for day 6 part 2

with open("day6\\input.txt", 'r') as file:
    text = file.read().splitlines()

times = text[0][13::]
Racetime = (int)("".join(times.split()))

distances = text[1][11::].split()
distance = (int)("".join(distances))

recordBroken = 0

start_time = time.perf_counter()

for i in range(Racetime):
    distanceCovered = i * (Racetime - i)
    if distanceCovered > distance:
        recordBroken += 1

end_time = time.perf_counter()
elapsed_time = end_time - start_time

print(recordBroken)
print("elapsed time : {} seconds".format(elapsed_time))

# answer = 34123437
# elapsed time : 44.06448629964143 seconds