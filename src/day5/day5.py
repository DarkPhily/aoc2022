crate_arrangement = []
crate_movement = []


def sanitize_input():
    arrangement = []
    movement = []
    with open("./data.txt", 'r') as data:
        is_movement = False
        for line in data:
            if line == '\n':
                arrangement.pop()
                is_movement = True
            elif is_movement:
                movement.append(line.split())
            else:
                arrangement.append(line.replace('    ', ' [] ').split())

    arrangement = [list(x) for x in zip(*arrangement)]
    for index, item in enumerate(arrangement):
        item.reverse()
        arrangement[index] = list(filter(lambda x: x != '[]', item))
    return arrangement, movement


def first_movement(arrangement, movement):
    for line in movement:
        amount = int(line[1])
        start_stack = int(line[3]) - 1
        end_stack = int(line[5]) - 1
        while amount != 0:
            arrangement[end_stack].append(arrangement[start_stack].pop())
            amount -= 1
    return arrangement


def second_movement(arrangement, movement):
    for line in movement:
        amount = int(line[1])
        start_stack = int(line[3]) - 1
        end_stack = int(line[5]) - 1
        whole_stack = []
        while amount != 0:
            whole_stack.append((arrangement[start_stack].pop()))
            amount -= 1
        whole_stack.reverse()
        for crate in whole_stack:
            arrangement[end_stack].append(crate)
    return arrangement


def get_top_crates(arrangement):
    return ''.join(stack.pop().replace('[', '').replace(']', '') for stack in arrangement)


if __name__ == '__main__':
    crate_arrangement, crate_movement = sanitize_input()
    result = first_movement(crate_arrangement, crate_movement)
    print(f'First answer: {get_top_crates(result)}')

    crate_arrangement, crate_movement = sanitize_input()
    result = second_movement(crate_arrangement, crate_movement)
    print(f'Second answer: {get_top_crates(result)}')
