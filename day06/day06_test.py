import unittest

from day06.day06 import day06


class Day06TestCase(unittest.TestCase):
    def test(self):
        lines = [
            '123 328  51 64 ',
            ' 45 64  387 23 ',
            '  6 98  215 314',
            '*   +   *   +  '
        ]
        self.assertEqual(4277556, day06(lines))


if __name__ == '__main__':
    unittest.main()
