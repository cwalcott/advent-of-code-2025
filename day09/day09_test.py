import unittest

from day09.day09 import day09, day09_part2


class Day09TestCase(unittest.TestCase):
    def setUp(self):
        self.lines = ['7,1', '11,1', '11,7', '9,7', '9,5', '2,5', '2,3', '7,3']

    def test_part1(self):
        self.assertEqual(50, day09(self.lines))

    # def test_part2(self):
    #     self.assertEqual(25272, day09_part2(self.lines))


if __name__ == '__main__':
    unittest.main()
