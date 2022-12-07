from collections import Counter

with open("./data.txt", 'r') as data:
    input_data = data.readlines()


def is_marker(buffer):
    count = Counter(buffer)
    return len(buffer) == len(count)


def iterate_input(buffer_length):
    buffer = []
    count_chars = 0
    for line in input_data:
        for char in line:
            count_chars += 1
            if len(buffer) == buffer_length:
                buffer.pop(0)
                buffer.append(char)
                if is_marker(buffer):
                    return count_chars
            else:
                buffer.append(char)


if __name__ == '__main__':
    print(f'First answer: {iterate_input(4)}')
    print(f'Second answer: {iterate_input(14)}')
