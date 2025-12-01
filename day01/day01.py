def day01(rotations: list[str]) -> int:
    dial, zero_count = 50, 0

    for rotation in rotations:
        direction, number = rotation[0:1], int(rotation[1:])
        match direction:
            case 'L':
                dial = (dial + number) % 100
            case 'R':
                dial = (dial - number) % 100
            case _:
                raise f'Invalid direction ${direction}'

        if dial == 0:
            zero_count += 1

    return zero_count


if __name__ == "__main__":
    with open('input', 'r') as f:
        lines = f.readlines()
        print(day01(lines))
