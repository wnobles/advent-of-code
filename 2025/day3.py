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

with open("2025/data/day3_input.txt") as f:
    read_data = f.read().splitlines()
print(part1(read_data))
