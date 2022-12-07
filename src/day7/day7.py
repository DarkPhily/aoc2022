directory_content = {}
file_size = 0
current_directory = ''


def get_input():
    with open("./data.txt", 'r') as data:
        return data.readlines()


def get_total_size(directory):
    if 'child_dirs' not in directory_content[directory]:
        return int(directory_content[directory].get('size'))
    size = sum(get_total_size(child) for child in directory_content[directory].get('child_dirs'))

    directory_content[directory]['size'] += size
    return directory_content[directory]['size']


def find_directory(size, comparision):
    if comparision == 'at most':
        return [directory for directory in directory_content if directory_content[directory].get('size') <= size]
    elif comparision == 'at least':
        return [directory for directory in directory_content if directory_content[directory].get('size') >= size]


def get_size(dirs):
    sizes = [directory_content[directory].get('size') for directory in dirs]
    sizes = sorted(sizes, reverse=True)
    return sizes[-1]


if __name__ == '__main__':
    current_directory = ""
    input_data = get_input()
    for line in input_data:
        split_line = line.split()
        if split_line[0] == '$':
            if split_line[1] == 'cd' and split_line[2] != '..':
                if current_directory == '':
                    current_directory = f'{current_directory}{split_line[2]}'
                else:
                    current_directory = f'{current_directory}{split_line[2]}/'
                directory_content[current_directory] = {}
            elif split_line[1] == 'ls':
                continue
            elif split_line[1] == 'cd':
                parent_directories = current_directory.split('/')
                parent_directory = f"{'/'.join(parent_directories[:-2])}/"
                current_directory = parent_directory
        elif split_line[0] == 'dir':
            directory_content[current_directory].setdefault('child_dirs', [])
            directory_content[current_directory].setdefault('size', 0)
            directory_content[current_directory]['child_dirs'].append(f'{current_directory}{split_line[1]}/')
        elif split_line[0].isnumeric():
            directory_content[current_directory].setdefault('size', 0)
            directory_content[current_directory]['size'] += int(split_line[0])
    directory_content['/']['size'] = get_total_size('/')

    size_sum = sum(directory_content[directory].get('size') for directory in find_directory(100000, 'at most'))
    print(f'First answer: {size_sum}')

    free_space = 70000000 - directory_content['/'].get('size')
    at_least_needed_space = 30000000 - free_space
    directories = find_directory(at_least_needed_space, 'at least')

    print(f'First answer: {get_size(directories)}')




