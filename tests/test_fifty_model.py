# -*- coding: utf-8 -*-
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from fifty_model import get_layout, count_vertices


class TestFiftyModel(unittest.TestCase):
    def test_layout_size(self):
        layout = get_layout()
        self.assertEqual(len(layout), 9)

    def test_real_virtual(self):
        layout = get_layout()
        real = [k for k, v in layout.items() if v["type"] == "实"]
        virtual = [k for k, v in layout.items() if v["type"] == "虚"]
        self.assertEqual(len(real), 5)
        self.assertEqual(len(virtual), 4)

    def test_vertices(self):
        self.assertEqual(count_vertices(), 32)


if __name__ == "__main__":
    unittest.main()
