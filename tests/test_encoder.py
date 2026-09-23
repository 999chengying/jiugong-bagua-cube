# -*- coding: utf-8 -*-
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from jiugong_encoder import classify_tetra
from pruning import prune_candidates, reverse_three_harmony


class TestEncoder(unittest.TestCase):
    def test_sheng(self):
        r = classify_tetra([1, 6, 7, 8])
        self.assertEqual(r["form"], "生")

    def test_heng(self):
        r = classify_tetra([1, 4, 7, 8])
        self.assertEqual(r["form"], "恒")

    def test_kong_face(self):
        r = classify_tetra([1, 3, 6, 8])
        self.assertEqual(r["form"], "空")

    def test_zheng_si_mian_ti(self):
        r = classify_tetra([3, 6, 9, 2])
        self.assertEqual(r["form"], "恒")

    def test_prune_parent_retreat(self):
        grouped = prune_candidates(1, [6, 7, 8, 9])
        self.assertIn("生", grouped)

    def test_reverse_three_harmony(self):
        self.assertEqual(reverse_three_harmony(6), [[1, 2, 3, 6]])


if __name__ == "__main__":
    unittest.main()
