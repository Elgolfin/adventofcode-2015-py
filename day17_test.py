"""
Day 17 unit tests
"""

import unittest
import day17_lib

class Day17TestCase(unittest.TestCase):
    """
    Tests for `day13_lib.py`
    """

    def test_parse_input(self):
        """
        Tests for the parse_input method
        """

        input_lines = [
            """12
11
190
0""",
            """""",
        ]
        expected = [
            [12, 11, 190, 0],
            [],
        ]
        for index, case in enumerate(input_lines):
            ints = day17_lib.parse_input(case)
            self.assertListEqual(ints, expected[index])

    def test_get_exact_combinations(self):
        """
        Tests for the get_exact_combinations method
        """

        input_containers = [
            [20, 15, 10, 5, 5],
        ]
        input_capacities = [
            25,
        ]
        expected = [
            4,
        ]
        for index, containers in enumerate(input_containers):
            res = day17_lib.get_exact_combinations(input_capacities[index], containers)
            self.assertEqual(res, expected[index])

    def test_get_exact_min_combinations(self):
        """
        Tests for the get_exact_combinations method
        """

        input_containers = [
            [20, 15, 10, 5, 5],
        ]
        input_capacities = [
            25,
        ]
        expected = [
            3,
        ]
        for index, containers in enumerate(input_containers):
            res = day17_lib.get_exact_combinations(input_capacities[index], containers, True)
            self.assertEqual(res, expected[index])

if __name__ == '__main__':
    unittest.main()
