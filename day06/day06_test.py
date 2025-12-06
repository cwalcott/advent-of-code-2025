import unittest

from day06.day06 import day06, day06_part2


class Day06TestCase(unittest.TestCase):
    def setUp(self):
        self.lines = [
            '123 328  51 64 ',
            ' 45 64  387 23 ',
            '  6 98  215 314',
            '*   +   *   +  '
        ]

    def test(self):
        self.assertEqual(4277556, day06(self.lines))

    def test_part2(self):
        self.assertEqual(3263827, day06_part2(self.lines))


if __name__ == '__main__':
    unittest.main()
