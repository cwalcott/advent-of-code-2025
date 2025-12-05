import unittest

from day04.day04 import day04, day04_part2


class Day04TestCase(unittest.TestCase):
    def setUp(self):
        self.rolls = [
            '..@@.@@@@.',
            '@@@.@.@.@@',
            '@@@@@.@.@@',
            '@.@@@@..@.',
            '@@.@@@@.@@',
            '.@@@@@@@.@',
            '.@.@.@.@@@',
            '@.@@@.@@@@',
            '.@@@@@@@@.',
            '@.@.@@@.@.'
        ]

    def test_sample(self):
        self.assertEqual(13, day04(self.rolls))

    def test_sample_part2(self):
        self.assertEqual(43, day04_part2(self.rolls))


if __name__ == '__main__':
    unittest.main()
