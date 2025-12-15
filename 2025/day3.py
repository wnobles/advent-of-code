def part1(data: list) -> int:

    num = 0
    for line in data:
        first_digit = str(max(map(int, line)))
        first_idx = line.index(str(first_digit))

        if first_idx == len(line) - 1:
            remaining_line = line[:first_idx]
            second_digit = first_digit
            first_digit = str(max(map(int, remaining_line)))
        else:
            remaining_line = line[first_idx+1:]
            second_digit = str(max(map(int, remaining_line)))

        num += int(first_digit + second_digit)

    return num

def part2(data: list) -> int:

    num = 0
    for line in data:

        digits = ""
        counter = 11
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

        num += int(digits)

    return num


with open("2025/data/day3_input.txt") as f:
    read_data = f.read().splitlines()
print(f"Part1: {part1(read_data)}")
print(f"Part2: {part2(read_data)}")
