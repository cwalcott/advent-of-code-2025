import unittest

from day11.day11 import day11, day11_part2


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

    def test_part2(self):
        lines = [
            'svr: aaa bbb',
            'aaa: fft',
            'fft: ccc',
            'bbb: tty',
            'tty: ccc',
            'ccc: ddd eee',
            'ddd: hub',
            'hub: fff',
            'eee: dac',
            'dac: fff',
            'fff: ggg hhh',
            'ggg: out',
            'hhh: out'
        ]

        self.assertEqual(2, day11_part2(lines))


if __name__ == '__main__':
    unittest.main()
