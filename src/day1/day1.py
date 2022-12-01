import numpy as np

all_elves_calories = []
elves_calories = []

with open("data.txt", 'r') as data:
    for line in data:
        if line == "\n":
            all_elves_calories.append(elves_calories)
            elves_calories = []
        else:
            calories = int(line.strip("\n"))
            elves_calories.append(calories)

total_calories_per_elve = [np.sum(elves_calories) for elves_calories in all_elves_calories]

print(f"Answer 1: {np.amax(total_calories_per_elve)}")

sorted_elves = np.sort(total_calories_per_elve)
print(f"Answer 2: {np.sum(sorted_elves[-3:])}")
