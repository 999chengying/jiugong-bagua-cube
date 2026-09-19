# -*- coding: utf-8 -*-
import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from jiugong_encoder import classify_tetra
from pruning import prune_candidates, reverse_three_harmony


class TestEncoder(unittest.TestCase):
    def test_sheng(self):
        r = classify_tetra([1, 6, 7, 8])
        self.assertEqual(r["form"], "生")
        self.assertAlmostEqual(r["volume"], 1 / 6)

    def test_heng(self):
        r = classify_tetra([1, 4, 7, 8])
        self.assertEqual(r["form"], "恒")
        self.assertAlmostEqual(r["volume"], 1 / 3)

    def test_kong_face(self):
        r = classify_tetra([1, 3, 6, 8])
        self.assertTrue(r["coplanar"])
        self.assertEqual(r["form"], "空")
        self.assertEqual(r["volume"], 0.0)

    def test_kong_diag(self):
        r = classify_tetra([1, 3, 7, 9])
        self.assertTrue(r["coplanar"])
        self.assertEqual(r["coplanar_type"], "对角截面")

    def test_zheng_si_mian_ti(self):
        r = classify_tetra([3, 6, 9, 2])
        self.assertEqual(r["form"], "恒")
        self.assertAlmostEqual(r["volume"], 1 / 3)

    def test_hua(self):
        r = classify_tetra([2, 6, 7, 8])
        self.assertEqual(r["form"], "化")

    def test_bian(self):
        r = classify_tetra([1, 4, 6, 7])
        self.assertEqual(r["form"], "变")

    def test_prune_parent_retreat(self):
        grouped = prune_candidates(1, [6, 7, 8, 9])
        self.assertIn("生", grouped)
        self.assertEqual(len(grouped["生"]), 1)
        self.assertEqual(grouped["生"][0]["numbers"], [1, 6, 7, 8])

    def test_reverse_three_harmony(self):
        self.assertEqual(reverse_three_harmony(6), [[1, 2, 3, 6]])
        self.assertEqual(reverse_three_harmony(4), [[4, 7, 8, 9]])


if __name__ == "__main__":
    unittest.main()
