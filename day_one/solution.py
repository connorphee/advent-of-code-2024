import unittest
from typing import List, Tuple
from math import prod
from collections import Counter
from io_utils.functions import columns_to_lists

class DayOneSolution:
    def part_one(self, input: Tuple[List[int], List[int]]) -> int:
        sorted_one = sorted(input[0])
        sorted_two = sorted(input[1])
        return sum(abs(a - b) for a,b in zip(sorted_one, sorted_two))

    def part_two(self, input: Tuple[List[int], List[int]]) -> int:
        counts = Counter(input[1])
        return sum(x * counts.get(x, 0) for x in input[0])

class DayOneUnitTest(unittest.TestCase):

    def setUp(self):
        self.solution = DayOneSolution()

    def test_part_one_example(self):
        list_one = [3, 4, 2, 1, 3, 3]
        list_two = [4, 3, 5, 3, 9, 3]

        self.assertEqual(11, self.solution.part_one((list_one, list_two)))

    def test_part_one_input(self):
        input_lists = columns_to_lists('./day_one/input.txt')
        self.assertEqual(2031679, self.solution.part_one(input_lists))

    def test_part_two_example(self):
        list_one = [3, 4, 2, 1, 3, 3]
        list_two = [4, 3, 5, 3, 9, 3]

        self.assertEqual(31, self.solution.part_two((list_one, list_two)))

    def test_part_two_input(self):
        input_lists = columns_to_lists('./day_one/input.txt')
        self.assertEqual(19678534, self.solution.part_two(input_lists))

        
if __name__ == '__main__':
    unittest.main()
