def day11(lines: list[str]) -> int:
    devices = {}
    for line in lines:
        device, remaining = line.split(': ', 2)
        children = remaining.split(' ')

        devices[device] = children

    def dfs(node: str) -> int:
        if node == 'out':
            return 1
        else:
            result = 0
            for child in devices[node]:
                result += dfs(child)
            return result

    return dfs('you')


if __name__ == "__main__":
    with open('input', 'r') as f:
        lines = [line.strip() for line in f]
        print(day11(lines))
