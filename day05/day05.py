def day05(lines: list[str]) -> int:
    count = 0
    ranges = []

    for line in lines:
        if '-' in line:
            start, end = line.split('-')
            ranges.append((int(start), int(end)))
        elif line:
            id = int(line)
            for start, end in ranges:
                if start <= id <= end:
                    count += 1
                    break

    return count


if __name__ == "__main__":
    with open('input', 'r') as f:
        lines = [line.strip() for line in f]
        print(day05(lines))
