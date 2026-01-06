def part1(data: list) -> int:

    # Keep track of the number of splits
    splits = 0

    # Keep a set of indices of tachyon beams for shared beam locations
    beams_indices = set()

    # Append the first tachyon beam location at S
    first_beam = data[0].find("S")
    if first_beam != -1:
        beams_indices.add(first_beam)

    # Iterate over the remaining rows
    for row in data[1:]:

        for i, c in enumerate(row):

            # If a splitter is encountered...
            if c == "^":
        
                # 1. Remove a beam index at the same location
                if i in beams_indices:
                    beams_indices.remove(i)

                    # a. Splits are counted when beams encounter a splitter
                    # (i.e., the element is removed from the list)
                    splits += 1

                # 2. Add the new beam locations to the set
                beams_indices.update([i - 1, i + 1])

    return splits

with open("2025/data/day7_input.txt") as f:
    read_data = [line.rstrip("\n") for line in f]
# print(read_data)

print(part1(read_data))
