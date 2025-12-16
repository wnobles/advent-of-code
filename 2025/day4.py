def get_removed_rolls(data: list, remove_once: bool = True) -> int:

    num_rolls = 0

    coords_list = [
        (i, j) for i, line in enumerate(data) for j, x in enumerate(line)
        if x == "@"]
    coords_to_remove = []

    for i, (a, b) in enumerate(coords_list):

        search_list = coords_list[:i] + coords_list[i+1:]

        adjacent_count = sum(
            abs(a - c) <= 1 and abs(b - d) <= 1
            for j, (c, d) in enumerate(search_list))

        if adjacent_count < 4:
            num_rolls += 1
            coords_to_remove.append((a, b))

    if remove_once:
        return num_rolls

    while coords_to_remove:

        coords_list = [
            item for item in coords_list if item not in coords_to_remove]
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

    return num_rolls

with open("2025/data/day4_input.txt") as f:
    read_data = f.read().splitlines()

print(f"Part 1: {get_removed_rolls(read_data, remove_once=True)}")
print(f"Part 2: {get_removed_rolls(read_data, remove_once=False)}")
