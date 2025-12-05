import unittest

from day05.day05 import day05


class Day05TestCase(unittest.TestCase):
    def test(self):
        lines = ['3-5', '10-14', '16-20', '12-18', '', '1', '5', '8', '11', '17', '32']
        self.assertEqual(3, day05(lines))


if __name__ == '__main__':
    unittest.main()
