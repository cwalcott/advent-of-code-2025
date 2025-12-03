import unittest

from day03.day03 import largest_joltage, day03, largest_joltage_part2


class Day03TestCase(unittest.TestCase):
    def test_joltage1(self):
        self.assertEqual(98, largest_joltage('987654321111111'))

    def test_joltage1_part2(self):
        self.assertEqual(987654321111, largest_joltage_part2('987654321111111'))

    def test_joltage2(self):
        self.assertEqual(89, largest_joltage('811111111111119'))

    def test_joltage2_part2(self):
        self.assertEqual(811111111119, largest_joltage_part2('811111111111119'))

    def test_joltage3(self):
        self.assertEqual(78, largest_joltage('234234234234278'))

    def test_joltage3_part2(self):
        self.assertEqual(434234234278, largest_joltage_part2('234234234234278'))

    def test_joltage4(self):
        self.assertEqual(92, largest_joltage('818181911112111'))

    def test_joltage5(self):
        self.assertEqual(88, largest_joltage('3881'))

    def test_joltage6(self):
        self.assertEqual(89, largest_joltage('789'))

    def test_day01(self):
        self.assertEqual(357, day03(['987654321111111', '811111111111119', '234234234234278', '818181911112111']))

if __name__ == '__main__':
    unittest.main()
