

def largest_joltage(bank: str) -> int:
    digits = []
    for i in range(len(bank)):
        num = int(bank[i])
        if len(digits) < 2:
            digits.append(num)
        elif i == len(bank) - 1:
            if num > digits[1]:
                if digits[1] > digits[0]:
                    digits = [digits[1], num]
                else:
                    digits[1] = num
        elif i < len(bank) - 1 and num > digits[0] and num > digits[1]:
            digits = [num]
        elif num > digits[0]:
            digits = [digits[1], num]
        elif num > digits[1]:
            digits = [digits[0], num]

    return digits[0] * 10 + digits[1]


def day03(banks: list[str]) -> int:
    result = 0
    for bank in banks:
        result += largest_joltage(bank)

    return result


if __name__ == "__main__":
    with open('input', 'r') as f:
        lines = [line.strip() for line in f]
        print(day03(lines))
