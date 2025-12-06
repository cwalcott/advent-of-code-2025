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


if __name__ == "__main__":
    with open('input', 'r') as f:
        lines = [line.strip() for line in f]
        print(day06(lines))
