def day07(lines: list[str]) -> int:
    lines = [list(line) for line in lines]
    splits = 0

    for i in range(len(lines) - 1):
        line = lines[i]
        if 'S' in line:
            lines[i + 1][line.index('S')] = '|'
        else:
            for idx, c in enumerate(line):
                if c == '|':
                    if lines[i + 1][idx] == '^':
                        splits += 1
                        lines[i + 1][idx - 1] = '|'
                        lines[i + 1][idx + 1] = '|'
                    else:
                        lines[i + 1][idx] = '|'

    return splits


if __name__ == "__main__":
    with open('input', 'r') as f:
        lines = [line.strip() for line in f]
        print(day07(lines))
