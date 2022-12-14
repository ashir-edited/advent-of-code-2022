# read line
# split into two
# find common items
# sum up the priorities
count = 1
with open("input.txt", "r") as f:
    priorities = []
    for line in f:
        current_priority_count = 0

        trimmed_line = line[:-1]  # remove newline from string
        split = int(len(trimmed_line) / 2)
        first_compartment = trimmed_line[0:split]
        second_compartment = trimmed_line[split:]

        first_compartment_set = set(first_compartment)
        second_compartment_set = set(second_compartment)

        common_items = first_compartment_set.intersection(second_compartment_set)
        for item in common_items:
            if item.isupper():
                current_priority_count += ord(item) - 38
            else:
                current_priority_count += ord(item) - 96
        priorities.append(current_priority_count)
        count += 1
    print(sum(priorities))
