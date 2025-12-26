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

def part2(problems: list, operators: list) -> int:

    result = 0

    for i, operator in enumerate(operators):
        if operator == "*":
            product = 1
            for num in problems[i]:
                product *= int(num)
            result += product
        else:
            result += sum(list(map(int, problems[i])))

    return result

with open("2025/data/day6_input.txt") as f:
    read_data = [line.rstrip("\n") for line in f]

operators = read_data.pop(-1)

problem_ranges = []
operator_start = 0
for i, c in enumerate(operators[1:], 1):
    if c in ["*", "+"]:
        problem_ranges.append([operator_start, i - 1])
        operator_start = i
problem_ranges.append([operator_start, i + 1])

problems = []
for start, stop in problem_ranges:
    problem = []
    for i in range(start, stop):
        num = "".join(line[i] for line in read_data).strip()
        problem.append(num)
    problems.append(problem)

operators = operators.split()

print(f"Part 2: {part2(problems, operators)}")
