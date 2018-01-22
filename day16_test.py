"""
Day 16 unit tests
"""

import unittest
import day16_lib

class Day16TestCase(unittest.TestCase):
    """
    Tests for `day13_lib.py`
    """

    def test_parse_aunt_line(self):
        """
        Tests for the parse aunt line
        """

        aunt_lines = [
            'Sue 1: goldfish: 9, cars: 0, samoyeds: 9',
            'Sue 2: perfumes: 5, trees: 8, goldfish: 8',
            'Sue 3: pomeranians: 2, akitas: 1, trees: 5 ',
        ]
        expected = {
            1: {
                'goldfish': 9,
                'cars': 0,
                'samoyeds': 9,
            },
            2: {
                'perfumes': 5,
                'trees': 8,
                'goldfish': 8,
            },
            3: {
                'pomeranians': 2,
                'akitas': 1,
                'trees': 5,
            }
        }
        for line in aunt_lines:
            aunt_id, aunt = day16_lib.parse_aunt_line(line)
            self.assertDictEqual(aunt, expected[aunt_id])


    def test_matches(self):
        """
        Tests for the aunt match
        """
        ticker_tape = {
            'children': 3,
            'cats': 7,
            'samoyeds': 2,
            'pomeranians': 3,
            'akitas': 0,
            'vizslas': 0,
            'goldfish': 5,
            'trees': 3,
            'cars': 2,
            'perfumes': 1
        }
        no_matches_aunt = [
            {
                'children': 3,
                'cars': 0,
            },
            {'children': 0},
            {'akitas': 2},
            {'cars': 7},
        ]
        matches_aunt = [
            {'children': 3},
            {
                'goldfish': 5,
                'children': 3,
            },
            {'akitas': 0},
            {'cars': 2},
        ]
        for aunt in no_matches_aunt:
            self.assertFalse(day16_lib.matches(ticker_tape, aunt))
        for aunt in matches_aunt:
            self.assertTrue(day16_lib.matches(ticker_tape, aunt))

if __name__ == '__main__':
    unittest.main()
