import unittest

from day05.day05 import day05, day05_part2, merge_ranges


class Day05TestCase(unittest.TestCase):
    def setUp(self):
        self.lines = ['3-5', '10-14', '16-20', '12-18', '', '1', '5', '8', '11', '17', '32']

    def test(self):
        self.assertEqual(3, day05(self.lines))

    def test_part2(self):
        self.assertEqual(14, day05_part2(self.lines))

    def test_merge_ranges(self):
        self.assertEqual([(3, 5), (10, 20)], merge_ranges([(3, 5), (10, 14), (16, 20), (12, 18)]))


if __name__ == '__main__':
    unittest.main()
