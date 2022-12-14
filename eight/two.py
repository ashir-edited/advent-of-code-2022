def get_col(trees, col_index, row_index_to_ignore):
    up = []
    down = []
    for count, row in enumerate(trees):
        if count < row_index_to_ignore:
            up.append(row[col_index])
        elif count == row_index_to_ignore:
            pass
        else:
            down.append(row[col_index])

    return up, down


def convert_to_int(trees):
    converted_trees = []
    for row in trees:
        converted_trees.append([int(x) for x in row])
    return converted_trees


def get_viewing_score(trees, tree_size):
    if not trees:
        return 0
    else:
        viewing_distance = 0
        for tree in trees:
            viewing_distance += 1
            if tree >= tree_size:
                break
        return viewing_distance


with open("input.txt") as f:
    lines = f.readlines()
    trees = []
    for line in lines:
        line = line.rstrip()
        trees.append(list(line))
    trees = convert_to_int(trees)

    scores = []
    for row_index, row in enumerate(trees):
        for col_index, tree in enumerate(row):
            left = row[:col_index]
            right = row[col_index + 1:]
            up_col, down_col = get_col(trees, col_index, row_index)
            if left:
                left.reverse()
            if up_col:
                up_col.reverse()

            viewing_score = 1
            viewing_score *= get_viewing_score(up_col, tree)
            viewing_score *= get_viewing_score(down_col, tree)
            viewing_score *= get_viewing_score(left, tree)
            viewing_score *= get_viewing_score(right, tree)
            scores.append(viewing_score)
    print(max(scores))
