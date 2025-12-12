import unittest

from day11.day11 import day11


class Day11TestCase(unittest.TestCase):
    def test_part1(self):
        lines = [
            'aaa: you hhh',
            'you: bbb ccc',
            'bbb: ddd eee',
            'ccc: ddd eee fff',
            'ddd: ggg',
            'eee: out',
            'fff: out',
            'ggg: out',
            'hhh: ccc fff iii',
            'iii: out'
        ]

        self.assertEqual(5, day11(lines))


if __name__ == '__main__':
    unittest.main()
