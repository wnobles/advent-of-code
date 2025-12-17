def part1(ids: list, ranges: list) -> int:

    id_ranges = [range(start, stop) for start, stop in ranges]

    fresh_ids = 0

    for id in ids:
        fresh_ids += any(id in id_range for id_range in id_ranges)

    return fresh_ids

def part2(ranges: list) -> int:

    sorted_ranges = sorted(ranges)
    consolidated_ranges = [sorted_ranges.pop(0)]

    for start, stop in sorted_ranges:
        last_range = consolidated_ranges[-1]
        if start <= last_range[1]:
            last_range[1] = max(last_range[1], stop)
        else:
            consolidated_ranges.append([start, stop])

    fresh_ids = sum(
        [len(range(start, stop)) for start, stop in consolidated_ranges])

    return fresh_ids

with open("2025/data/day5_input.txt") as f:

    ingredient_range = f.readline().strip()
    ingredient_ranges = []
    while "-" in ingredient_range:
        start, stop = ingredient_range.split("-")
        ingredient_ranges.append([int(start), int(stop) + 1])
        ingredient_range = f.readline().strip()

    ingredient_id = f.readline().strip()
    ingredient_ids = []
    while ingredient_id:
        ingredient_ids.append(int(ingredient_id))
        ingredient_id = f.readline().strip()

print(f"Part 1: {part1(ingredient_ids, ingredient_ranges)}")
print(f"Part 2: {part2(ingredient_ranges)}")
