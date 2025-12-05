def get_zero_crossings(data: list) -> tuple[int, int]:
    total_landings = 0
    total_crossings = 0
    position = 50

    for line in data:
        dist = abs(line)
        next_pos = position + line
        next_pos_cycled = next_pos % 100

        # Part 1
        if next_pos_cycled == 0:
            total_landings += 1

        # Case 1: both zero positions
        if position == 0 and next_pos_cycled == 0:
            rotation = dist // 100
            total_crossings += rotation

        # Case 2: non-zero position, zero next position
        elif position != 0 and next_pos_cycled == 0:
            rotation = dist // 100 + 1 # add one for landing on zero
            total_crossings += rotation

        # Case 3: zero position, non-zero next position
        elif position == 0 and next_pos_cycled != 0:
            rotation = dist // 100
            total_crossings += rotation

        # Case 4: both non-zero positions
        else:
            rotation = dist // 100
            left_over = (dist % 100 if line > 0 else (dist % 100) * -1)
            remaining_dist = position + left_over
            extra = remaining_dist < 0 or remaining_dist > 100
            if (next_pos < 0 or next_pos > 100) and dist < 100:
                total_crossings += 1
            elif dist > 100:
                total_crossings += rotation + extra

        position = next_pos_cycled

    return total_landings, total_crossings

with open("2025/input.txt") as f:
    read_data = f.read().splitlines()
read_data = [int(x.replace("L", "-").replace("R", "")) for x in read_data]

print(f"Passwords (Part 1, Part 2): {get_zero_crossings(read_data)}")
