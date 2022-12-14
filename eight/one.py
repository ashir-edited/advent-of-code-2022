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


with open("input.txt") as f:
    lines = f.readlines()
    trees = []
    for line in lines:
        line = line.rstrip()
        trees.append(list(line))
    trees = convert_to_int(trees)

    count = 0
    for row_index, row in enumerate(trees):
        for col_index, tree in enumerate(row):
            left = row[:col_index]
            right = row[col_index + 1:]
            up_col, down_col = get_col(trees, col_index, row_index)

            is_visible = False
            if not left or not right or not up_col or not down_col:
                is_visible = True
            elif max(left) < tree:
                is_visible = True
            elif max(right) < tree:
                is_visible = True
            elif max(down_col) < tree:
                is_visible = True
            elif max(up_col) < tree:
                is_visible = True

            if is_visible:
                count += 1
    print(count)
