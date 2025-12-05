def get_zero_landings(data: list) -> int:
    total = 0
    position = 50
    for line in data:
        position = (position + line) % 100 # positions 0 to 99
        if position == 0:
            total += 1
    return total

def get_zero_crossings(data: list) -> int:
    total = 0
    position = 50

    for line in data:
        distance = position + line
        next_pos = distance % 100

        # Case 1: both zero positions
        if position == 0 and next_pos == 0:
            rotation = abs(line) // 100
            total += rotation

        # Case 2: non-zero position, zero next position
        elif position != 0 and next_pos == 0:
            rotation = abs(line) // 100 + 1 # add one for landing on zero
            total += rotation

        # Case 3: zero position, non-zero next position
        elif position == 0 and next_pos != 0:
            rotation = abs(line) // 100
            total += rotation

        # Case 4: both non-zero positions
        else:
            rotation = abs(line) // 100
            left_over = (abs(line) % 100 if line > 0 else (abs(line) % 100) * -1)
            extra = ((position + left_over) < 0) or ((position + left_over) > 100)
            if (distance < 0 or distance > 100) and (abs(line) < 100):
                total += 1
            elif abs(line) > 100:
                total += rotation + extra

        position = next_pos

    return total

with open("2025/input.txt") as f:
    read_data = f.read().splitlines()
read_data = [int(x.replace("L", "-").replace("R", "")) for x in read_data]

print(f"Part 1 password: {get_zero_landings(read_data)}")
print(f"Part 2 password: {get_zero_crossings(read_data)}")
