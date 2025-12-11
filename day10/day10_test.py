import unittest

from day10.day10 import day10, fewest_button_presses


class Day10TestCase(unittest.TestCase):
    def setUp(self):
        self.lines = [
            '[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}',
            '[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}',
            '[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}'
        ]

    def test_fewest_button_presses(self):
        self.assertEqual(2, fewest_button_presses({1, 2}, [{3}, {1, 3}, {2}, {2, 3}, {0, 2}, {0, 1}]))

    def test_fewest_button_presses_2(self):
        self.assertEqual(3, fewest_button_presses({3}, [{0, 2, 3, 4}, {2, 3}, {0, 4}, {0, 1, 2}, {1, 2, 3, 4}]))

    def test_fewest_button_presses_3(self):
        self.assertEqual(
            2,
            fewest_button_presses({1, 2, 3, 5}, [{0, 1, 2, 3, 4}, {0, 3, 4}, {0, 1, 2, 4, 5}, {1, 2}, {1, 2, 3, 4}]))

    def test_fewest_button_presses_4(self):
        self.assertEqual(
            5,
            fewest_button_presses(
                {1, 2},
                [{0, 1, 3, 4, 6, 7, 8}, {1, 2, 3, 5, 6, 8}, {0, 1}, {3, 5, 6, 7}, {2, 5, 7}, {1, 2, 3, 4, 5, 7, 8}, {7},
                 {0, 1, 3}, {0, 3, 7}, {1, 4, 6}]))

    def test_fewest_button_presses_5(self):
        self.assertEqual(
            7,
            fewest_button_presses(
                {0, 1, 8},
                [{1, 3, 5, 6, 7, 8}, {1, 2, 6, 7}, {0, 6}, {0, 3, 4, 5, 6, 8}, {9, 4}, {0, 1, 2, 3, 4, 5, 6, 7, 8},
                 {0, 3, 4, 6, 8, 9}, {1, 4, 6, 7}, {0, 4}, {1, 2, 4, 5, 8}, {1, 2, 5}]))

    def test_part1(self):
        self.assertEqual(7, day10(self.lines))


if __name__ == '__main__':
    unittest.main()
