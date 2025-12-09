def area(a: tuple[int, int], b: tuple[int, int]) -> int:
    return abs(a[0] - b[0] + 1) * abs(a[1] - b[1] + 1)


def day09(lines: list[str]) -> int:
    tiles: list[tuple[int, int]] = []
    for line in lines:
        x, y = line.split(',')
        tiles.append((int(x), int(y)))

    largest = -1
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            largest = max(largest, area(tiles[i], tiles[j]))
    return largest


def day09_part2(lines: list[str]) -> int:
    pass


if __name__ == "__main__":
    with open('input', 'r') as f:
        lines = [line.strip() for line in f]
        print(day09(lines))
        print(day09_part2(lines))
