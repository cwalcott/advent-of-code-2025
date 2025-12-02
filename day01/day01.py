def day01(rotations: list[str]) -> int:
    dial, count = 50, 0

    for rotation in rotations:
        direction, number = rotation[0:1], int(rotation[1:])
        match direction:
            case 'L':
                dial -= number
            case 'R':
                dial += number
            case _:
                raise f'Invalid direction ${direction}'

        dial %= 100

        if dial == 0:
            count += 1

    return count


def day01_434C49434B(rotations: list[str]) -> int:
    dial, count = 50, 0

    for rotation in rotations:
        direction, number = rotation[0:1], int(rotation[1:])
        match direction:
            case 'L':
                while number > 0:
                    dial -= 1
                    number -= 1
                    if dial == 0:
                        count += 1
                    elif dial == -1:
                        dial = 99
            case 'R':
                while number > 0:
                    dial += 1
                    number -= 1
                    if dial == 100:
                        count += 1
                        dial = 0
            case _:
                raise f'Invalid direction ${direction}'

    return count


if __name__ == "__main__":
    with open('input', 'r') as f:
        lines = [line.strip() for line in f]
        print(day01(lines))
        print(day01_434C49434B(lines))
