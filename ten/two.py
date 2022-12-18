def simulate_cycle(cycle, x, rows, amount=0, cycle_twice=False):
    row = (cycle - 1) // 40
    index = (cycle - 1) % 40

    if index in range(x - 1, x + 2):
        rows[row].append("#")
    else:
        rows[row].append(".")

    cycle += 1

    if not cycle_twice:
        return cycle, x, rows

    row = (cycle - 1) // 40
    index = (cycle - 1) % 40

    if index in range(x - 1, x + 2):
        rows[row].append("#")
    else:
        rows[row].append(".")

    cycle += 1
    x += amount

    return cycle, x, rows


with open("input.txt") as f:
    x = 1
    cycle = 1
    rows = []
    for i in range(6):
        rows.append([])

    for line in f:
        line = line.rstrip()
        instruction = line.split()
        command = instruction[0]

        if command == "noop":
            cycle, x, row = simulate_cycle(cycle, x, rows)
        elif command == "addx":
            cycle, x, rows = simulate_cycle(cycle, x, rows, int(instruction[1]), cycle_twice=True)

for row in rows:
    print("".join(row))
