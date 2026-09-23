# -*- coding: utf-8 -*-
"""剪枝规则库。"""

import os
import sys
from itertools import combinations

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from jiugong_encoder import classify_tetra, COORDS


def parent_retreat(pole, combo):
    if pole in (1, 2, 3, 4) and 9 in combo:
        return False
    if pole in (6, 7, 8, 9) and 1 in combo:
        return False
    return True


def prune_candidates(pole, opposite_vertices, include_empty=False):
    if pole not in COORDS or pole == 5:
        raise ValueError("极点必须是1-9且不含5")

    candidates = []
    for combo in combinations(opposite_vertices, 3):
        combo = list(combo)
        if 5 in combo or pole in combo or len(set(combo)) != 3:
            continue
        if not parent_retreat(pole, combo):
            continue
        four = [pole] + combo
        result = classify_tetra(four)
        if not result["valid"]:
            continue
        if result["form"] == "空" and not include_empty:
            continue
        candidates.append(result)

    grouped = {}
    for c in candidates:
        grouped.setdefault(c["form"], []).append(c)
    return grouped


def reverse_three_harmony(generating_number):
    mapping = {6: [1, 2, 3], 4: [7, 8, 9]}
    if generating_number not in mapping:
        return []
    return [sorted(mapping[generating_number] + [generating_number])]


if __name__ == "__main__":
    import json
    result = prune_candidates(1, [6, 7, 8, 9])
    print(json.dumps(result, ensure_ascii=False, indent=2))
