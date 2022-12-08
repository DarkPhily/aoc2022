grid = []


def get_input():
    with open("./data.txt", 'r') as data:
        for line in data:
            line = line.replace('\n', '')
            tree_line = list(line)
            grid.append(tree_line)


def is_tree_visible():
    visible_trees = 0
    for tree_line_index, tree_line in enumerate(grid):
        for tree_index, tree in enumerate(tree_line):
            if tree_line_index in [0, len(grid) - 1] or tree_index in [0, len(tree_line) - 1]:
                visible_trees += 1
                continue
            elif all(tree > grid[tree_line_index][i] for i in range(tree_index)):
                visible_trees += 1
                continue
            elif all(tree > grid[tree_line_index][i] for i in range(tree_index + 1, len(tree_line))):
                visible_trees += 1
                continue
            elif all(tree > grid[i][tree_index] for i in range(tree_line_index)):
                visible_trees += 1
                continue
            elif all(tree > grid[i][tree_index] for i in range(tree_line_index + 1, len(grid))):
                visible_trees += 1
                continue
    return visible_trees


def get_score():
    score_list = []
    for tree_line_index, tree_line in enumerate(grid):
        score_list.append([])
        for tree_index, tree in enumerate(tree_line):
            score = 0
            view_left = 0
            view_right = 0
            view_top = 0
            view_bottom = 0
            if tree_line_index in [0, len(grid) - 1] or tree_index in [0, len(tree_line) - 1]:
                score = 0
                score_list[tree_line_index].append(score)
                continue
            for i in range(tree_index - 1, -1, -1):
                view_left += 1
                if tree <= grid[tree_line_index][i]:
                    break
            for i in range(tree_index + 1, len(tree_line)):
                view_right += 1
                if tree <= grid[tree_line_index][i]:
                    break
            for i in range(tree_line_index - 1, -1, -1):
                view_top += 1
                if tree <= grid[i][tree_index]:
                    break
            for i in range(tree_line_index + 1, len(grid)):
                view_bottom += 1
                if tree <= grid[i][tree_index]:
                    break
            score = view_left * view_right * view_top * view_bottom
            score_list[tree_line_index].append(score)
    return score_list


def get_best_tree():
    best_tree_per_line = [max(tree_line) for tree_line in scores]
    return max(best_tree_per_line)


if __name__ == "__main__":
    get_input()
    print(is_tree_visible())
    scores = get_score()
    print(get_best_tree())