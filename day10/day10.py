from collections import deque


def fewest_button_presses(desired_lights: set[int], buttons: list[set[int]]) -> int:
    seen = set()
    queue = deque([([], set())])
    while queue:
        path, lights = queue.popleft()

        if lights == desired_lights:
            return len(path)
        else:
            for button in buttons:
                new_lights = lights ^ button
                if tuple(new_lights) not in seen:
                    seen.add(tuple(new_lights))
                    queue.append((path + [lights], new_lights))

    return -1


def day10(lines: list[str]) -> int:
    total = 0
    for i, line in enumerate(lines):
        desired_lights_str, *schematics, _ = line.split(' ')

        desired_lights = set()
        for i in range(1, len(desired_lights_str) - 1):
            if desired_lights_str[i] == '#':
                desired_lights.add(i - 1)

        buttons = []
        for schematic_str in schematics:
            schematic = eval(schematic_str)
            if type(schematic) is tuple:
                buttons.append(set(schematic))
            else:
                buttons.append({schematic})

        total += fewest_button_presses(desired_lights, buttons)

    return total


def fewest_button_presses_part2(desired_counters: list[int], buttons: list[set[int]]) -> int:
    memo = {}

    def dfs(counters):
        nonlocal memo

        key = tuple(counters)
        if key in memo:
            return memo[key]

        if all(c == 0 for c in counters):
            memo[key] = 0
        else:
            shortest = float('inf')

            for button in buttons:
                new_counters = counters[:]
                for i in button:
                    new_counters[i] -= 1

                if all(c >= 0 for c in new_counters):
                    shortest = min(shortest, dfs(new_counters) + 1)

            memo[key] = shortest

        return memo[key]

    result = dfs(desired_counters)
    if type(result) is int:
        return result
    else:
        return -1


def day10_part2(lines: list[str]) -> int:
    total = 0
    for i, line in enumerate(lines):
        print(f"On line {i + 1} of {len(lines)}")

        _, *schematics, desired_counters_str = line.split(' ')

        buttons = []
        for schematic_str in schematics:
            schematic = eval(schematic_str)
            if type(schematic) is tuple:
                buttons.append(set(schematic))
            else:
                buttons.append({schematic})

        desired_counters = list(map(int, desired_counters_str[1:-1].split(',')))

        total += fewest_button_presses_part2(desired_counters, buttons)

    return total


if __name__ == "__main__":
    with open('input', 'r') as f:
        lines = [line.strip() for line in f]
        print(day10(lines))
        print(day10_part2(lines))
