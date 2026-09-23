# -*- coding: utf-8 -*-
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from cycle_analysis import analyze_cycle


class TestCycle(unittest.TestCase):
    def test_k5_forms(self):
        r = analyze_cycle(5, "子")
        forms = [c["form"] for c in r["circles_detail"]]
        self.assertEqual(forms, ["变", "生", "化", "生", "变"])

    def test_k6_zheng(self):
        r = analyze_cycle(6, "子")
        forms = [c["form"] for c in r["circles_detail"]]
        self.assertEqual(forms, ["空"])

    def test_k6_wei(self):
        r = analyze_cycle(6, "未")
        forms = [c["form"] for c in r["circles_detail"]]
        self.assertEqual(forms, ["空"])

    def test_k9_heng(self):
        r = analyze_cycle(9, "子")
        self.assertEqual(r["circles"], 3)
        self.assertEqual(r["segments"], 8)


if __name__ == "__main__":
    unittest.main()
