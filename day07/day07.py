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


def day07_part2(lines: list[str]) -> int:
    memo = {}

    def number_of_paths(lines_start: int, particle_position: int) -> int:
        if (lines_start, particle_position) in memo:
            return memo[(lines_start, particle_position)]

        if lines_start > len(lines) - 1:
            result = 1
        elif lines[lines_start][particle_position] == '^':
            result = (number_of_paths(lines_start + 1, particle_position - 1) +
                      number_of_paths(lines_start + 1, particle_position + 1))
        else:
            result = number_of_paths(lines_start + 1, particle_position)

        memo[(lines_start, particle_position)] = result
        return result

    return number_of_paths(1, lines[0].index('S'))


if __name__ == "__main__":
    with open('input', 'r') as f:
        lines = [line.strip() for line in f]
        print(day07(lines))
        print(day07_part2(lines))
