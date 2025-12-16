def part1(ids: list, ranges: list) -> int:

    fresh_ids = 0

    for id in ids:
        fresh_ids += any(id in id_range for id_range in ranges)

    return fresh_ids

with open("2025/data/day5_input.txt") as f:

    ingredient_range = f.readline().strip()
    ingredient_ranges = []
    while "-" in ingredient_range:
        start, stop = ingredient_range.split("-")
        ingredient_ranges.append(range(int(start), int(stop) + 1))
        ingredient_range = f.readline().strip()

    ingredient_id = f.readline().strip()
    ingredient_ids = []
    while ingredient_id:
        ingredient_ids.append(int(ingredient_id))
        ingredient_id = f.readline().strip()

print(f"Part 1: {part1(ingredient_ids, ingredient_ranges)}")
