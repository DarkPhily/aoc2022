from string import ascii_lowercase, ascii_uppercase

# Create values for the priority
values = {f'{char}': i for i, char in enumerate(ascii_lowercase, 1)}
for i, char in enumerate(ascii_uppercase, 27):
    values[f'{char}'] = i

duplicate_items = []

with open("./data.txt", 'r') as data:
    for line in data:
        first_compartment = line[:len(line)//2]
        second_compartment = line[len(line)//2:]
        for char in first_compartment:
            if char in second_compartment:
                duplicate_items.append(char)
                break

print(f"First answer: {sum(values[f'{_}'] for _ in duplicate_items)}")


first_line = ''
second_line = ''
third_line = ''
group_badge = []
with open("./data.txt", 'r') as data:
    for counter, line in enumerate(data):
        if counter % 3 == 0:
            first_line = line.strip()
            continue
        if counter % 3 == 1:
            second_line = line.strip()
            continue
        if counter % 3 == 2:
            third_line = line.strip()
        for char in first_line:
            if char in second_line and char in third_line:
                group_badge.append(char)
                break

print(f"Second answer: {sum(values[f'{_}'] for _ in group_badge)}")

