with open("input.txt") as f:
    x = 1
    cycle = 1
    total = []
    checks = [20, 60, 100, 140, 180, 220]
    for line in f:
        line = line.rstrip()
        instruction = line.split()
        command = instruction[0]

        if cycle in checks:
            total.append(x * cycle)

        if command == "noop":
            cycle += 1
        elif command == "addx":
            cycle += 2
            if cycle - 1 in checks:
                total.append(x * (cycle - 1))
            amount = int(instruction[1])
            x += amount

print(sum(total))
