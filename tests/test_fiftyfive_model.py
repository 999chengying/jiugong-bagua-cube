# -*- coding: utf-8 -*-
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from fiftyfive_model import count_positions, FIFTYFIVE_STRUCTURE


class TestFiftyFiveModel(unittest.TestCase):
    def test_total(self):
        self.assertEqual(count_positions(), 55)

    def test_six_directions(self):
        dirs = FIFTYFIVE_STRUCTURE["六个立方体"]
        self.assertEqual(len(dirs), 6)

    def test_center(self):
        self.assertEqual(FIFTYFIVE_STRUCTURE["中心合一"], 10)


if __name__ == "__main__":
    unittest.main()
