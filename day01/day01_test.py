import unittest

from day01.day01 import day01, day01_434C49434B


class Day01TestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(3, day01(['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']))

    def test_434C49434B(self):
        self.assertEqual(6, day01_434C49434B(['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']))


if __name__ == '__main__':
    unittest.main()
