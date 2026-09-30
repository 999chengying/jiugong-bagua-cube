# -*- coding: utf-8 -*-
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from four_images import get_four_images, get_generation_chain


class TestFourImages(unittest.TestCase):
    def test_numbers(self):
        images = get_four_images()
        self.assertEqual(images["老阴"]["number"], 24)
        self.assertEqual(images["少阳"]["number"], 28)
        self.assertEqual(images["少阴"]["number"], 32)
        self.assertEqual(images["老阳"]["number"], 36)

    def test_chain(self):
        chain = get_generation_chain()
        self.assertEqual(chain, ["老阴", "少阳", "少阴", "老阳"])

    def test_centers(self):
        images = get_four_images()
        self.assertEqual(images["老阴"]["wuji_centers"], 0)
        self.assertEqual(images["少阳"]["wuji_centers"], 4)
        self.assertEqual(images["少阴"]["wuji_centers"], 0)
        self.assertEqual(images["老阳"]["wuji_centers"], 4)


if __name__ == "__main__":
    unittest.main()
