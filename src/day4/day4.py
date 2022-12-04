completely_included = 0

with open("./data.txt", 'r') as data:
    for line in data:
        first, second = line.split(',')
        first_start, first_stop = list(map(int, first.split('-')))
        second_start, second_stop = list(map(int, second.split('-')))
        if second_start >= first_start and second_stop <= first_stop or first_start >= second_start and first_stop <= second_stop:
            completely_included += 1

print(f"First answer: {completely_included}")

partial_included = 0

with open("./data.txt", 'r') as data:
    for line in data:
        first, second = line.split(',')
        first_start, first_stop = list(map(int, first.split('-')))
        second_start, second_stop = list(map(int, second.split('-')))
        if (first_start >= second_start or first_stop >= second_start) and (second_start >= first_start or second_stop >= first_start):
            partial_included += 1

print(f"Second answer: {partial_included}")
