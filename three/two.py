with open("input.txt", "r") as f:
    priorities = []
    while True:
        elf_one = f.readline()
        if elf_one == "":
            break
        else:
            elf_one = set(elf_one[:-1])
        elf_two = set(f.readline()[:-1])
        elf_three = set(f.readline()[:-1])
        current_priority_count = 0

        badge = elf_one.intersection(elf_two).intersection(elf_three).pop()
        if badge.isupper():
            priorities.append(ord(badge) - 38)
        else:
            priorities.append(ord(badge) - 96)
    print(sum(priorities))
