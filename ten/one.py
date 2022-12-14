with open("input.txt") as f:
    x = 1
    cycle = 1
    total = []
    checks = [20, 60, 100, 140, 180, 220]
    for line in f:
        line = line.rstrip()
        instruction = line.split()
        command = instruction[0]

        if cycle == 20:
            total.append(x * 20)
        elif cycle == 60:
            total.append(x * 60)
        elif cycle == 100:
            total.append(x * 100)
        elif cycle == 140:
            total.append(x * 140)
        elif cycle == 180:
            total.append(x * 180)
        elif cycle == 220:
            total.append(x * 220)

        if command == "noop":
            cycle += 1
        elif command == "addx":
            cycle += 2
            if cycle - 1 in checks:
                print(cycle)
                total.append(x * (cycle - 1))
            amount = int(instruction[1])
            x += amount

print(sum(total))
print(total)
