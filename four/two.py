with open("input.txt") as f:
    count = 0
    for line in f:
        pairs = line.rstrip().split(",")
        pairs = line.split(",")
        pair_one = pairs[0].split("-")
        pair_one = [int(x) for x in pair_one]

        pair_two = pairs[1].split("-")
        pair_two = [int(x) for x in pair_two]

        pair_one_items = [*range(pair_one[0], pair_one[1] + 1)]
        pair_two_items = [*range(pair_two[0], pair_two[1] + 1)]

        if not set(pair_one_items).isdisjoint(set(pair_two_items)):
            count += 1
    print(count)
