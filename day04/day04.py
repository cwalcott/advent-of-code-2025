def day04(rolls: list[str]) -> int:
    if not rolls or not rolls[0]:
        return 0

    count = 0
    n = len(rolls)
    m = len(rolls[0])

    for x in range(n):
        for y in range(m):
            if rolls[x][y] == '@':
                adj_rolls = 0
                if x > 0:
                    if y > 0 and rolls[x - 1][y - 1] == '@':
                        adj_rolls += 1
                    if rolls[x - 1][y] == '@':
                        adj_rolls += 1
                    if y < m - 1 and rolls[x - 1][y + 1] == '@':
                        adj_rolls += 1
                if y > 0 and rolls[x][y - 1] == '@':
                    adj_rolls += 1
                if y < m - 1 and rolls[x][y + 1] == '@':
                    adj_rolls += 1
                if x < n - 1:
                    if y > 0 and rolls[x + 1][y - 1] == '@':
                        adj_rolls += 1
                    if rolls[x + 1][y] == '@':
                        adj_rolls += 1
                    if y < m - 1 and rolls[x + 1][y + 1] == '@':
                        adj_rolls += 1

                if adj_rolls < 4:
                    count += 1

    return count


if __name__ == "__main__":
    with open('input', 'r') as f:
        lines = [line.strip() for line in f]
        print(day04(lines))
