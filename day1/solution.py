import unittest
from typing import List


class DayOneSolution:
    def find_difference(self, list_one: List[int], list_two: List[int]) -> int:
        sorted_one = sorted(list_one)
        sorted_two = sorted(list_two)
        return sum(abs(a - b) for a,b in zip(sorted_one, sorted_two))


class DayOneUnitTest(unittest.TestCase):

    def test_example(self):
        list_one = [3, 4, 2, 1, 3, 3]
        list_two = [4, 3, 5, 3, 9, 3]

        self.assertEqual(11, DayOneSolution().find_difference(list_one, list_two))

    def test_input(self):
        list_one = []
        list_two = []
        with open('day1/input.txt') as file:
            for line in file:
                split = line.strip().split("   ")
                if(len(split) == 2): 
                    list_one.append(int(split[0]))
                    list_two.append(int(split[1]))

        self.assertEqual(2031679, DayOneSolution().find_difference(list_one, list_two))

        
        
if __name__ == '__main__':
    unittest.main()
