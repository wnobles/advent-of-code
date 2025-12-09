def get_invalid_ids(data: list) -> int:

    repeated_twice = 0
    repeated = 0

    for line in data:
        start, stop = line.split("-")
        start, stop = int(start), int(stop)

        for i in range(start, stop + 1):
            num = str(i)
            if len(num) > 1:

                # Largest repeating sequence is half the length
                largest_repeat = len(num) // 2

                # Look at progressively smaller chunks
                for j in range(largest_repeat, 0, -1):
                    digits_list = [
                        num[k:k+j]
                        for k in range(0, len(num), j)]
                    if len(set(digits_list)) == 1:
                        if j == largest_repeat and len(num) % 2 == 0:
                            repeated_twice += i
                            repeated += i
                        else:
                            repeated += i
                        break

    return repeated_twice, repeated

with open("2025/data/day2_input.txt") as f:
    read_data = f.read()
read_data = read_data.split(",")

print(f"Invalid IDs (Part 1, Part 2): {get_invalid_ids(read_data)}")
