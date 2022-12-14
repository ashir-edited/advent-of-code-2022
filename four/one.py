with open("input.txt") as f:
    count = 0
    for line in f:
        pairs = line[:-1].split(",")
        pair_one = pairs[0].split("-")
        pair_one = [int(x) for x in pair_one]

        pair_two = pairs[1].split("-")
        pair_two = [int(x) for x in pair_two]

        if pair_one[0] >= pair_two[0] and pair_one[1] <= pair_two[1]:
            count += 1
        elif pair_two[0] >= pair_one[0] and pair_two[1] <= pair_one[1]:
            count += 1
    print(count)
