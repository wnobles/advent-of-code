def part1(data: list) -> int:

    num_rolls = 0

    coords_list = [
        (i, j) for i, line in enumerate(data) for j, x in enumerate(line)
        if x == "@"]

    for i, (a, b) in enumerate(coords_list):

        search_list = coords_list[:i] + coords_list[i+1:]

        adjacent_count = sum(
            abs(a - c) <= 1 and abs(b - d) <= 1
            for j, (c, d) in enumerate(search_list))

        if adjacent_count < 4:
            num_rolls += 1

    return num_rolls

def part2(data: list) -> int:

    num_rolls = 0

    coords_list = [
        (i, j) for i, line in enumerate(data) for j, x in enumerate(line)
        if x == "@"]

    while 1:

        coords_to_remove = []
        for i, (a, b) in enumerate(coords_list):

            search_list = coords_list[:i] + coords_list[i+1:]

            adjacent_count = 0
            for j, (c, d) in enumerate(search_list):
                if abs(a - c) <= 1 and abs(b - d) <= 1:
                    adjacent_count += 1

            if adjacent_count < 4:
                num_rolls += 1
                coords_to_remove.append((a, b))

        if coords_to_remove:
            coords_list = [
                item for item in coords_list if item not in coords_to_remove]
        else:
            break

    return num_rolls

with open("2025/data/day4_input.txt") as f:
    read_data = f.read().splitlines()

print(f"Part 1: {part1(read_data)}")
print(f"Part 2: {part2(read_data)}")
