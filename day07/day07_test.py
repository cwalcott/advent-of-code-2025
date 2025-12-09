import unittest

from day07.day07 import day07, day07_part2


class Day07TestCase(unittest.TestCase):
    def setUp(self):
        self.lines = [
            '.......S.......',
            '...............',
            '.......^.......',
            '...............',
            '......^.^......',
            '...............',
            '.....^.^.^.....',
            '...............',
            '....^.^...^....',
            '...............',
            '...^.^...^.^...',
            '...............',
            '..^...^.....^..',
            '...............',
            '.^.^.^.^.^...^.',
            '...............'
        ]

    def test_part1(self):
        self.assertEqual(21, day07(self.lines))

    def test_part2(self):
        self.assertEqual(40, day07_part2(self.lines))


if __name__ == '__main__':
    unittest.main()
