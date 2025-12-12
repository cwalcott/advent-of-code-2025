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


def day11_part2(lines: list[str]) -> int:
    devices = {}
    for line in lines:
        device, remaining = line.split(': ', 2)
        children = remaining.split(' ')

        devices[device] = children

    devices['out'] = []

    def dfs(node: str, dst: str) -> int:
        memo = {}

        def dfs_with_memo(node: str, dst: str) -> int:
            if node not in memo:
                if node == dst:
                    memo[node] = 1
                else:
                    result = 0
                    for child in devices[node]:
                        result += dfs_with_memo(child, dst)
                    memo[node] = result

            return memo[node]

        return dfs_with_memo(node, dst)

    return (dfs('svr', 'fft') * dfs('fft', 'dac') * dfs('dac', 'out') +
            dfs('svr', 'dac') * dfs('dac', 'fft') * dfs('fft', 'out'))


if __name__ == "__main__":
    with open('input', 'r') as f:
        lines = [line.strip() for line in f]
        print(day11(lines))
        print(day11_part2(lines))
