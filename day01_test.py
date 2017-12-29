"""Day 01 unit tests"""

import unittest
from day01_lib import walk_through_floors

class Day01TestCase(unittest.TestCase):
    """Tests for `day01.py`"""

    def test_(self):
        """Tests for the final floor"""
        floor, enter_basement_at = walk_through_floors("(()))")
        self.assertEqual(floor, -1)
        self.assertEqual(enter_basement_at, 5)

if __name__ == '__main__':
    unittest.main()
