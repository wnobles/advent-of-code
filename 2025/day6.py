def calculate_problems_sum(file_path: str, right_to_left: bool = False) -> int:

    with open(file_path) as f:
        read_data = [line.rstrip("\n") for line in f]

    operators = read_data.pop(-1)

    # Get the beginning and ending indices of each "column" of digits
    problem_ranges = []
    operator_start = 0
    for i, c in enumerate(operators[1:], 1):
        if c in ["*", "+"]:
            problem_ranges.append([operator_start, i - 1]) # i-1 to ignore space
            operator_start = i
    problem_ranges.append([operator_start, i + 1]) # i+1 for exclusive end

    # Collect the digits in the columns vertically right to left or row by row
    problems = []
    for start, stop in problem_ranges:
        if right_to_left:
            problem = []
            for i in range(start, stop):
                num = "".join(line[i] for line in read_data).strip()
                problem.append(num)
        else:
            problem = [line[start:stop].strip() for line in read_data]
        problems.append(problem)

    operators = operators.split()

    result = 0

    # Do the math
    for i, operator in enumerate(operators):
        if operator == "*":
            product = 1
            for num in problems[i]:
                product *= int(num)
            result += product
        else:
            result += sum(list(map(int, problems[i])))

    return result

file_path = "2025/data/day6_input.txt"
print(f"Part 1: {calculate_problems_sum(file_path)}")
print(f"Part 2: {calculate_problems_sum(file_path, True)}")
