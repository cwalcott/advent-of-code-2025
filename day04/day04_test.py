import unittest

from day04.day04 import day04


class Day04TestCase(unittest.TestCase):
    def test_sample(self):
        rolls = [
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
        self.assertEqual(13, day04(rolls))


if __name__ == '__main__':
    unittest.main()
