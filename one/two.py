with open("input.txt", "r") as f:
    highest_calories = [0, 0, 0]
    current_count = 0
    for line in f:
        if line == "":
            if current_count > min(highest_calories):
                highest_calories.sort()
                highest_calories[0] = current_count
            break
        elif line == "\n":
            if current_count > min(highest_calories):
                highest_calories.sort()
                highest_calories[0] = current_count
            current_count = 0
        else:
            current_count += int(line)
    print(sum(highest_calories))  # answer is 208191
