import timeit

start_time = timeit.default_timer()
all_elves_calories = []
elves_calories = []

with open("./data.txt", 'r') as data:
    for line in data:
        if line == "\n":
            all_elves_calories.append(elves_calories)
            elves_calories = []
        else:
            calories = int(line.strip("\n"))
            elves_calories.append(calories)

total_calories_per_elf = [sum(elves_calories) for elves_calories in all_elves_calories]

print(f"Answer 1: {max(total_calories_per_elf)}")

total_calories_per_elf.sort()
print(f"Answer 2: {sum(total_calories_per_elf[-3:])}")

end_time = timeit.default_timer()
print(end_time - start_time)
