def part1(data: list) -> int:

    id_sum = 0

    for line in data:
        start, stop = line.split("-")
        start, stop = int(start), int(stop)

        for i in range(start, stop + 1):
            len_num = len(str(i))
            if len_num > 1 and len_num % 2 == 0:
                mod_amt = 10 ** (len_num / 2)
                first_half = i % mod_amt
                second_half = i // mod_amt
                if first_half == second_half:
                    id_sum += i

    return id_sum

with open("2025/data/day2_input.txt") as f:
    read_data = f.read()
read_data = read_data.split(",")
print(part1(read_data))
