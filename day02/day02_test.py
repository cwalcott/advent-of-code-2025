import unittest

from day02.day02 import day02


class Day02TestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(1227775554, day02(
            '11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'))


if __name__ == '__main__':
    unittest.main()
