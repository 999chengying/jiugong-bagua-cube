# -*- coding: utf-8 -*-
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from fault_tolerance import check_paths, infer_fault


class TestFaultTolerance(unittest.TestCase):
    def test_fault_3(self):
        status = check_paths(3)
        self.assertFalse(status["四正阳行"]["通"])
        self.assertTrue(status["四维阴行"]["通"])
        self.assertFalse(status["连续3阳行"]["通"])
        self.assertTrue(status["连续3阴行"]["通"])

    def test_infer_3(self):
        self.assertEqual(infer_fault(3), 3)

    def test_fault_1(self):
        status = check_paths(1)
        self.assertFalse(status["四正阳行"]["通"])
        self.assertFalse(status["连续3阳行"]["通"])
        self.assertFalse(status["连续2阴行"]["通"])
        self.assertFalse(status["阴功正四面体"]["通"])


if __name__ == "__main__":
    unittest.main()
