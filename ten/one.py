def simulate_cycle(cycle, x, amount=0, cycle_twice=False):
    checks = [20, 60, 100, 140, 180, 220]
    check = None

    if cycle in checks:
        check = x * cycle

    cycle += 1

    if not cycle_twice:
        return cycle, x, check

    if cycle in checks:
        check = x * cycle

    cycle += 1
    x += amount

    return cycle, x, check


with open("input.txt") as f:
    x = 1
    cycle = 1
    total = []

    for line in f:
        line = line.rstrip()
        instruction = line.split()
        command = instruction[0]

        if command == "noop":
            cycle, x, check = simulate_cycle(cycle, x)
        elif command == "addx":
            cycle, x, check = simulate_cycle(cycle, x, int(instruction[1]), cycle_twice=True)

        if check:
            total.append(check)

print(sum(total))
