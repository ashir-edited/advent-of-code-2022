with open("input.txt") as f:
    lines = f.readlines()
    stack_count_line = 8
    instruction_lines_start = 10
    number_of_stacks = len("".join(lines[stack_count_line].rstrip().split()))

    stacks = []
    for i in range(0, number_of_stacks):
        stacks.append([])

    for line in lines[0: stack_count_line]:
        for i, char in enumerate(line):
            if char.lower().isalpha():
                index = int((i - 1) / 4)
                stacks[index].append(char)

    for stack in stacks:
        stack.reverse()

    for line in lines[instruction_lines_start:]:
        instruction = line.rsplit()

        num_crates_to_move = int(instruction[1])
        crate_start = int(instruction[3]) - 1
        crate_end = int(instruction[5]) - 1

        for i in range(0, num_crates_to_move):
            crate_to_move = stacks[crate_start].pop()
            stacks[crate_end].append(crate_to_move)

    for stack in stacks:
        print(stack[-1], end="")
