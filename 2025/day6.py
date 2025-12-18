def part1(numbers: list, operators: list) -> int:

    result = 0

    num_problems = len(numbers[0])
    for i in range(num_problems):
        problem_numbers = [row[i] for row in numbers]
        operator = operators[i]
        if operator == "*":
            product = 1
            for num in problem_numbers:
                product *= num
            result += product
        else:
            result += sum(problem_numbers)

    return result

with open("2025/data/day6_input.txt") as f:
    numbers = []
    for line in f:
        if "*" not in line and "+" not in line:
            number_row = list(map(int, line.split()))
            numbers.append(number_row)
    operators = line.split()

print(f"Part 1: {part1(numbers, operators)}")
