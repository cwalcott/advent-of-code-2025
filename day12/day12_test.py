import unittest

from day12.day12 import day12, Shape, can_fit


class Day12TestCase(unittest.TestCase):
    def test_can_fit(self):
        shape = Shape.from_str('###\n#..\n###')

        self.assertTrue(can_fit(4, 4, [shape], {0: 1}))
        self.assertTrue(can_fit(4, 4, [shape], {0: 2}))
        self.assertFalse(can_fit(4, 4, [shape], {0: 3}))

    def test_can_fit_2(self):
        shapes = [
            Shape.from_str('###\n##.\n##.'),
            Shape.from_str('###\n##.\n.##'),
            Shape.from_str('.##\n###\n##.'),
            Shape.from_str('##.\n###\n##.'),
            Shape.from_str('###\n#..\n###'),
            Shape.from_str('###\n.#.\n###'),
        ]

        self.assertFalse(can_fit(12, 5, shapes, {0: 1, 1: 0, 2: 1, 3: 0, 4: 3, 5: 2}))

    def test_shape_from_str(self):
        self.assertEqual(
            ((True, True, True), (False, True, False), (False, False, True)), Shape.from_str('###\n.#.\n..#').value
        )

    def test_shape_str(self):
        self.assertEqual(
            "###\n.#.\n..#", str(Shape(value=((True, True, True), (False, True, False), (False, False, True))))
        )

    def test_shape_rotate_clockwise(self):
        self.assertEqual(Shape.from_str('..#\n.##\n#.#'), Shape.from_str('###\n.#.\n..#').rotate_clockwise())

    def test_shape_rotations(self):
        shape = Shape.from_str('###\n#..\n###')
        self.assertEqual(
            {
                Shape.from_str('###\n#..\n###'),
                Shape.from_str('###\n#.#\n#.#'),
                Shape.from_str('###\n..#\n###'),
                Shape.from_str('#.#\n#.#\n###')
            },
            shape.rotations()
        )

    def test_add_to_board(self):
        shape = Shape.from_str('###\n#.#\n#.#')
        board = [[False] * 4 for _ in range(4)]

        self.assertTrue(shape.add_to_board(board, 2, 0) is None)

        board = shape.add_to_board(board, 0, 0)
        self.assertEqual(
            [
                [True, True, True, False],
                [True, False, True, False],
                [True, False, True, False],
                [False, False, False, False]
            ],
            board)

        board = Shape.from_str('#.#\n#.#\n###').add_to_board(board, 1, 1)
        self.assertEqual(
            [
                [True, True, True, False],
                [True, True, True, True],
                [True, True, True, True],
                [False, True, True, True]
            ],
            board)

    def test_part1(self):
        lines = [
            '0:',
            '###',
            '##.',
            '##.',
            '',
            '1:',
            '###',
            '##.',
            '.##',
            '',
            '2:',
            '.##',
            '###',
            '##.',
            '',
            '3:',
            '##.',
            '###',
            '##.',
            '',
            '4:',
            '###',
            '#..',
            '###',
            '',
            '5:',
            '###',
            '.#.',
            '###',
            '',
            '4x4: 0 0 0 0 2 0',
            '12x5: 1 0 1 0 2 2',
            '12x5: 1 0 1 0 3 2',
        ]

        self.assertEqual(2, day12(lines))


if __name__ == '__main__':
    unittest.main()
