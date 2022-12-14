def move_head(current_head_position, direction):
    x = current_head_position[0]
    y = current_head_position[1]
    if direction == "L":
        x -= 1
    elif direction == "R":
        x += 1
    elif direction == "U":
        y += 1
    elif direction == "D":
        y -= 1

    new_position = (x, y)
    return new_position


def move_tail(tail_position, head_position):
    old_position = tail_position
    x_tail = tail_position[0]
    y_tail = tail_position[1]

    x_head = head_position[0]
    y_head = head_position[1]

    x_dif = x_head - x_tail
    y_dif = y_head - y_tail

    # prepare for some spaghetti
    if abs(x_dif) in [0, 1] and abs(y_dif) in [0, 1]:  # do nothing, the head is adjacent to the tail
        return tail_position, tail_position
    elif abs(x_dif) == 2 and abs(y_dif) == 0:  # simply move left or right
        if x_dif > 0:
            return (x_tail + 1, y_tail), old_position
        else:
            return (x_tail - 1, y_tail), old_position
    elif abs(y_dif) == 2 and abs(x_dif) == 0:  # simply move up or down
        if y_dif > 0:
            return (x_tail, y_tail + 1), old_position
        else:
            return (x_tail, y_tail - 1), old_position
    else:  # not adjacent and aren't in the same row or column. move diagonally
        # decide on up or down first, then left or right
        if x_dif > 0 and y_dif > 0:  # go up right
            return (x_tail + 1, y_tail + 1), old_position
        elif x_dif > 0 and y_dif < 0:  # go down right
            return (x_tail + 1, y_tail - 1), old_position
        elif x_dif < 0 and y_dif > 0:  # go up left
            return (x_tail - 1, y_tail + 1), old_position
        else:  # down left
            return (x_tail - 1, y_tail - 1), old_position


with open("input.txt") as f:
    coords_visited = []
    lines = f.readlines()

    last_tail_position = None
    head_position = (0, 0)
    tail_position = (0, 0)
    all_tails = [tail_position] * 9

    for line in lines:
        line = line.rstrip()
        instruction = line.split()

        direction = instruction[0]
        amount = int(instruction[1])
        for i in range(amount):
            head_position = move_head(head_position, direction)
            for count, tail in enumerate(all_tails):
                current_tail_position = tail
                new_tail_position = None
                if count == 0:
                    new_tail_position, last_tail_position = move_tail(current_tail_position, head_position)
                    all_tails[0] = new_tail_position
                else:
                    cur_head_position = all_tails[count - 1]
                    new_tail_position, last_tail_position = move_tail(current_tail_position, cur_head_position)
                    all_tails[count] = new_tail_position
                    if count == 8:
                        print(all_tails[count - 1], new_tail_position)
                        coords_visited.append(new_tail_position)

    coords_visited_set = set(coords_visited)
    print(len(coords_visited_set))
