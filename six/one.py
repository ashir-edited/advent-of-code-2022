with open("input.txt") as f:
    line = f.readline().rstrip()
    window = 14
    chars_processed = 0

    for i in range(len(line)):
        area = line[i:i + window]
        if len(area) == len(set(area)):
            chars_processed += window
            break
        else:
            chars_processed += 1
            i += 1
    print(chars_processed)
