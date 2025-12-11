from collections import deque


def fewest_button_presses(desired_lights: set[int], buttons: list[set[int]]) -> int:
    seen = set()
    queue = deque([([], set())])
    while queue:
        path, lights = queue.popleft()
        seen.add(tuple(lights))

        if lights == desired_lights:
            return len(path)
        else:
            for button in buttons:
                new_lights = lights ^ button
                if tuple(new_lights) not in seen:
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


if __name__ == "__main__":
    with open('input', 'r') as f:
        lines = [line.strip() for line in f]
        print(day10(lines))
