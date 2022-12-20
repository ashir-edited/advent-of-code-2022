import operator


ops = {
    "+": operator.add,
    "*": operator.mul,
}


def extract_items(line):
    line = line.split()[2:]
    numbers = [int(num.replace(",", "")) for num in line]
    return numbers


def extract_monkey_index(line):
    return int(line.split()[1].split(":")[0])


def extract_operation(line):
    operation = line.split("  Operation: ")[1].split()[2:]
    if operation[0] != "old":
        operation[0] = int(operation[0])
    if operation[2] != "old":
        operation[2] = int(operation[2])
    return operation


def extract_divisible_by(line):
    return int(line.split("  Test: divisible by ")[1])


def extract_true_monkey(line):
    return int(line.split("    If true: throw to monkey ")[1])


def extract_false_monkey(line):
    return int(line.split("    If false: throw to monkey ")[1])


def setup_monkeys(monkeys, lines):
    current_monkey_index = None
    for line in lines:
        if "Monkey" in line:
            current_monkey_index = extract_monkey_index(line)
        elif "Starting items" in line:
            monkeys[current_monkey_index]["items"] = extract_items(line)
        elif "Operation" in line:
            monkeys[current_monkey_index]["operation"] = extract_operation(line)
        elif "Test" in line:
            monkeys[current_monkey_index]["divisor"] = extract_divisible_by(line)
        elif "If true" in line:
            monkeys[current_monkey_index]["true_monkey"] = extract_true_monkey(line)
        elif "If false" in line:
            monkeys[current_monkey_index]["false_monkey"] = extract_false_monkey(line)


def calculate_new_worry_level(operation, current_worry_level):
    if operation[0] == "old":
        operand_one = current_worry_level
    if operation[2] == "old":
        operand_two = current_worry_level
    else:
        operand_two = operation[2]
    return ops[operation[1]](operand_one, operand_two) % 9699690


def get_target_monkey(worry_level, divisor, true_monkey, false_monkey):
    if worry_level % divisor == 0:
        return true_monkey
    else:
        return false_monkey


def throw_items(monkeys, source_monkey_index, items_and_targets):
    if not items_and_targets:
        pass

    source_monkey_items = monkeys[source_monkey_index]["items"]
    for item, target_monkey in items_and_targets:
        source_monkey_items.pop(0)
        target_monkey_items = monkeys[target_monkey]["items"]
        target_monkey_items.append(item)


with open("input.txt") as f:
    num_of_monkeys = 8
    monkeys = [{"inspections": 0} for _ in range(num_of_monkeys)]
    lines = [line.rstrip() for line in f]
    setup_monkeys(monkeys, lines)

    current_round = 0
    rounds = 10_000
    while current_round < rounds:
        current_round += 1
        for monkey_index, monkey in enumerate(monkeys):
            items_and_targets = []
            for item in monkey["items"]:
                monkey["inspections"] += 1
                new_worry_level = calculate_new_worry_level(monkey["operation"], item)
                target_monkey = get_target_monkey(
                    new_worry_level,
                    monkey["divisor"],
                    monkey["true_monkey"],
                    monkey["false_monkey"],
                )
                items_and_targets.append((new_worry_level, target_monkey))
            throw_items(monkeys, monkey_index, items_and_targets)

shenanigans = [monkey["inspections"] for monkey in monkeys]
shenanigans.sort()
shenanigans.reverse()
print(shenanigans)
print(shenanigans[0] * shenanigans[1])
