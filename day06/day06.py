import operator
from functools import reduce


def day06(lines: list[str]) -> int:
    nums: list[list[int]] = []
    for line in lines[:-1]:
        ints: list[int] = list(map(int, line.strip().split()))
        if not nums:
            nums = [[int] for int in ints]
        else:
            for i in range(len(ints)):
                nums[i].append(ints[i])

    result = 0
    ops = lines[-1].strip().split()
    for i, op in enumerate(ops):
        if op == '*':
            result += reduce(operator.mul, nums[i])
        elif op == '+':
            result += reduce(operator.add, nums[i])

    return result


def day06_part2(lines: list[str]) -> int:
    result = 0
    numbers = []
    columns = 0
    for line in lines:
        columns = max(columns, len(line))

    for column in range(columns - 1, -1, -1):
        cleaned = [line[column] for line in lines if column < len(line) and line[column] != ' ']
        if cleaned:
            num, op = 0, ''
            for element in cleaned:
                if element.isdigit():
                    num = (num * 10) + int(element)
                elif element == '+' or element == '*':
                    op = element

            numbers.append(num)
            if op == '*':
                result += reduce(operator.mul, numbers)
                numbers = []
            elif op == '+':
                result += reduce(operator.add, numbers)
                numbers = []

    return result


if __name__ == "__main__":
    with open('input', 'r') as f:
        lines = [line.strip() for line in f]
        print(day06(lines))
        print(day06_part2(lines))
