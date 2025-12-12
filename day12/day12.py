import copy
from copy import deepcopy
from dataclasses import dataclass
from itertools import batched


@dataclass(frozen=True)
class Shape:
    value: tuple[tuple[bool, ...], ...]

    @classmethod
    def from_str(cls, str_rep: str):
        lines = str_rep.strip().split('\n')
        value = tuple(tuple(c == '#' for c in line) for line in lines)
        return cls(value)

    def __str__(self):
        return '\n'.join(''.join('#' if cell else '.' for cell in row) for row in self.value)

    def height(self) -> int:
        return len(self.value)

    def width(self) -> int:
        return len(self.value[0]) if self.value else 0

    def rotate_clockwise(self):
        if not self.value:
            return Shape(())

        return Shape(
            value=tuple(
                tuple(
                    self.value[self.height() - 1 - row][col]
                    for row in range(self.height()))
                for col in range(self.width())
            )
        )

    def rotations(self):
        s = {self}
        cur = self
        for _ in range(3):
            cur = cur.rotate_clockwise()
            s.add(cur)

        return s

    def add_to_board(self, board: list[list[bool]], x: int, y: int) -> list[list[bool]] | None:
        if y + self.height() > len(board) or x + self.width() > len(board[0]):
            return None

        new_board = deepcopy(board)

        for i in range(self.width()):
            for j in range(self.height()):
                if self.value[i][j]:
                    if new_board[y + i][x + j]:
                        return None
                    else:
                        new_board[y + i][x + j] = True

        return new_board


def can_fit(width: int, height: int, shapes: list[Shape], counts: dict[int, int]) -> bool:
    rotations: dict[Shape, set[Shape]] = {}
    for shape in shapes:
        rotations[shape] = shape.rotations()

    seen = set()

    def dfs(board: list[list[bool]], counts: dict[int, int]) -> bool:
        # board_str = '\n'.join(''.join('#' if cell else '.' for cell in row) for row in board)
        # print(f"{counts=}")
        # print(f"{counts=} Considering:\n{board_str}")
        # print(f"{len(seen)=}")

        if all([x == 0 for x in counts.values()]):
            return True

        for shape_idx in [k for k, v in counts.items() if v > 0]:
            shape = shapes[shape_idx]
            for x in range(width - shape.width() + 1):
                for y in range(height - shape.height() + 1):
                    for r in rotations[shape]:
                        new_board = r.add_to_board(board, x, y)
                        if new_board:
                            new_board_str = '\n'.join(
                                ''.join('#' if cell else '.' for cell in row) for row in new_board
                            )
                            if new_board_str not in seen:
                                seen.add(new_board_str)
                                counts_copy = deepcopy(counts)
                                counts_copy[shape_idx] -= 1
                                if dfs(new_board, counts_copy):
                                    return True

        return False

    return dfs([[False] * width for _ in range(height)], counts)


def day12(lines: list[str]) -> int:
    sections = [[]]
    for line in lines:
        if line == '':
            sections.append([])
        else:
            sections[-1].append(line)

    shapes = []
    for section in sections[:-1]:
        shape = Shape.from_str("\n".join(section[0][1:]))

        shapes.append(shape)

    regions = []
    for line in sections[-1]:
        region, desired_shapes_str = line.split(': ')

        width, height = tuple(map(int, region.split('x')))

        desired_shapes = {}
        for i, e in enumerate(desired_shapes_str.split(' ')):
            desired_shapes[i] = int(e)

        regions.append((width, height, desired_shapes))

    count = 0
    for width, height, counts in regions:
        if can_fit(width, height, shapes, counts):
            count += 1

    return count


if __name__ == "__main__":
    with open('input', 'r') as f:
        lines = [line.strip() for line in f]
        print(day12(lines))
