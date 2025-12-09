import heapq
import math
import operator
from functools import reduce


def distance(p1: tuple[int, int, int], p2: tuple[int, int, int]) -> float:
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)


def day08(lines: list[str], pairs: int) -> int:
    distances = []
    points: list[tuple[int, int, int]] = []
    circuits: list[set[tuple[int, int, int]]] = []
    circuit_maps = {}
    for line in lines:
        x, y, z = map(int, line.split(',', 2))
        point = x, y, z
        for other in points:
            heapq.heappush(distances, (distance(point, other), point, other))
        points.append(point)
        circuits.append({point})
        circuit_maps[point] = len(circuits) - 1

    for _ in range(pairs):
        _, p1, p2 = heapq.heappop(distances)

        p1_circuit_index = circuit_maps[p1]
        p2_circuit_index = circuit_maps[p2]
        if p1_circuit_index != p2_circuit_index:
            circuits[p1_circuit_index] |= circuits[p2_circuit_index]
            for point in circuits[p2_circuit_index]:
                circuit_maps[point] = p1_circuit_index
            circuits[p2_circuit_index] = {}

    top_3_largest_circuits = sorted(map(len, circuits), reverse=True)[:3]

    return reduce(operator.mul, top_3_largest_circuits)


def day08_part2(lines: list[str]) -> int:
    distances = []
    points: list[tuple[int, int, int]] = []
    circuits: list[set[tuple[int, int, int]]] = []
    circuit_maps = {}
    circuit_indices = set()
    for line in lines:
        x, y, z = map(int, line.split(',', 2))
        point = x, y, z
        for other in points:
            heapq.heappush(distances, (distance(point, other), point, other))
        points.append(point)
        circuits.append({point})
        circuit_maps[point] = len(circuits) - 1
        circuit_indices.add(len(circuits) - 1)

    while distances:
        _, p1, p2 = heapq.heappop(distances)

        p1_circuit_index = circuit_maps[p1]
        p2_circuit_index = circuit_maps[p2]
        if p1_circuit_index != p2_circuit_index:
            circuits[p1_circuit_index] |= circuits[p2_circuit_index]
            for point in circuits[p2_circuit_index]:
                circuit_maps[point] = p1_circuit_index
            circuits[p2_circuit_index] = {}
            circuit_indices.remove(p2_circuit_index)

            if len(circuit_indices) == 1:
                return p1[0] * p2[0]

    return -1


if __name__ == "__main__":
    with open('input', 'r') as f:
        lines = [line.strip() for line in f]
        print(day08(lines, pairs=1000))
        print(day08_part2(lines))
