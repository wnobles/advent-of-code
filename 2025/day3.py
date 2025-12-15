def get_largest_joltages(data: list, batteries: int) -> int:

    total = 0
    for line in data:

        digits = ""
        counter = batteries - 1
        start = 0
        while counter >= 0:

            # Trim the list to be eleven, ten, nine, ..., zero away from the end
            end = len(line) - counter
            away_from_end = line[start:end]

            # Get the max value and index in the sub-string
            max_digit = str(max(map(int, away_from_end)))
            max_idx = away_from_end.index(max_digit)

            # Add the value to the string
            digits += max_digit

            # Increment the start and decrement the counter
            start += max_idx + 1
            counter -= 1

        total += int(digits)

    return total

with open("2025/data/day3_input.txt") as f:
    read_data = f.read().splitlines()
print(f"Part 1: {get_largest_joltages(read_data, 2)}")
print(f"Part 2: {get_largest_joltages(read_data, 12)}")
