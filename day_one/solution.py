import unittest
from typing import List
from math import prod
from collections import Counter


class DayOneSolution:
    def part_one(self, list_one: List[int], list_two: List[int]) -> int:
        sorted_one = sorted(list_one)
        sorted_two = sorted(list_two)
        return sum(abs(a - b) for a,b in zip(sorted_one, sorted_two))

    def part_two(self, list_one: List[int], list_two: List[int]) -> int:
        counts = Counter(list_two)
        return sum(x * counts.get(x, 0) for x in list_one)

class DayOneUnitTest(unittest.TestCase):

    def setUp(self):
        self.solution = DayOneSolution()

    def test_part_one_example(self):
        list_one = [3, 4, 2, 1, 3, 3]
        list_two = [4, 3, 5, 3, 9, 3]

        self.assertEqual(11, self.solution.part_one(list_one, list_two))

    def test_part_one_input(self):
        list_one = []
        list_two = []
        with open('./day_one/input.txt') as file:
            for line in file:
                split = line.strip().split("   ")
                if(len(split) == 2): 
                    list_one.append(int(split[0]))
                    list_two.append(int(split[1]))

        self.assertEqual(2031679, self.solution.part_one(list_one, list_two))

    def test_part_two_example(self):
        list_one = [3, 4, 2, 1, 3, 3]
        list_two = [4, 3, 5, 3, 9, 3]

        self.assertEqual(31, self.solution.part_two(list_one, list_two))

    def test_part_two_input(self):
        list_one = []
        list_two = []

        with open('./day_one/input.txt') as file:
            for line in file:
                split = line.strip().split("   ")
                if(len(split) == 2): 
                    list_one.append(int(split[0]))
                    list_two.append(int(split[1]))
        
        self.assertEqual(19678534, self.solution.part_two(list_one, list_two))

        
if __name__ == '__main__':
    unittest.main()
