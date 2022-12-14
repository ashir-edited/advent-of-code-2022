with open("input.txt", "r") as f:
    calorie_counts = []
    current_count = 0
    for line in f:
        if line == "":
            calorie_counts.append(current_count)
        elif line == "\n":
            calorie_counts.append(current_count)
            current_count = 0
        else:
            current_count += int(line)
    print(max(calorie_counts))  # answer is 71502
