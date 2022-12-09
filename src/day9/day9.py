instructions = []
tail_length = 9
with open("./data.txt", 'r') as data:
    instructions.extend(line.split() for line in data)


def adjust_tail(h, t):
    vertical_adjustment = (h[0] - t[0])
    horizontal_adjustment = (h[1] - t[1])
    if abs(vertical_adjustment) <= 1 and abs(horizontal_adjustment) <= 1:
        return t
    elif abs(vertical_adjustment) >= 2 and abs(horizontal_adjustment) >= 2:
        t = (h[0] - 1 if t[0] < h[0] else h[0] + 1, h[1] - 1 if t[1] < h[1] else h[1] + 1)
    elif abs(vertical_adjustment) >= 2:
        t = (h[0] - 1 if t[0] < h[0] else h[0] + 1, h[1])
    elif abs(horizontal_adjustment) >= 2:
        t = (h[0], h[1] - 1 if t[1] < h[1] else h[1] + 1)
    return t


if __name__ == '__main__':
    head = (0, 0)
    tail = [(0, 0) for _ in range(tail_length)]
    vertical = {'L': 0, 'U': -1, 'R': 0, 'D': 1}
    horizontal = {'L': -1, 'U': 0, 'R': 1, 'D': 0}
    part_1 = {tail[0]}
    part_2 = {tail[8]}
    for line in instructions:
        direction = line[0]
        amount = int(line[1])
        for _ in range(amount):
            head = (head[0] + vertical[direction], head[1] + horizontal[direction])
            tail[0] = adjust_tail(head, tail[0])
            for i in range(1, 9):
                tail[i] = adjust_tail(tail[i - 1], tail[i])
            part_1.add(tail[0])
            part_2.add(tail[8])
    print(f"First answer: {len(part_1)}")
    print(f"Second answer: {len(part_2)}")
