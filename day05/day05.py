def day05(lines: list[str]) -> int:
    count = 0
    ranges = []

    for line in lines:
        if '-' in line:
            start, end = line.split('-')
            ranges.append((int(start), int(end)))
        elif line:
            identifier = int(line)
            for start, end in ranges:
                if start <= identifier <= end:
                    count += 1
                    break

    return count


def merge_ranges(unmerged: list[tuple]) -> list[tuple[int, int]]:
    result = []
    unmerged.sort()

    for start, end in unmerged:
        if not result or result[-1][1] < start:
            result.append((start, end))
        else:
            result[-1] = (min(result[-1][0], start), max(result[-1][1], end))

    return result


def day05_part2(lines: list[str]) -> int:
    unmerged = [tuple(map(int, line.split('-'))) for line in lines if '-' in line]

    ranges = merge_ranges(unmerged)

    count = 0
    for range in ranges:
        count += range[1] - range[0] + 1

    return count


if __name__ == "__main__":
    with open('input', 'r') as f:
        lines = [line.strip() for line in f]
        print(day05(lines))
        print(day05_part2(lines))
