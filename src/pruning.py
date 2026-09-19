# -*- coding: utf-8 -*-
"""
剪枝规则库
"""

from itertools import combinations
from jiugong_encoder import classify_tetra, COORDS


def parent_retreat(pole, combo):
    """
    父母退位规则：
    - 极点在生数面 1,2,3,4 时，对面不选乾9；
    - 极点在成数面 6,7,8,9 时，对面不选坤1。
    """
    if pole in (1, 2, 3, 4) and 9 in combo:
        return False
    if pole in (6, 7, 8, 9) and 1 in combo:
        return False
    return True


def prune_candidates(pole, opposite_vertices, include_empty=False):
    """
    给定极点，从对面顶点中选三个，应用剪枝规则。
    返回按形态分组的字典。
    """
    if pole not in COORDS or pole == 5:
        raise ValueError("极点必须是1-9且不含5")

    candidates = []
    for combo in combinations(opposite_vertices, 3):
        combo = list(combo)
        if 5 in combo:
            continue
        if pole in combo:
            continue
        if len(set(combo)) != 3:
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
    """
    三合反推示例：
    - 生成数 6：二十四山中非父母退位形成的 6 在 1,2,3 宫，反推得 1236。
    - 生成数 4：二十四山中非父母退位形成的 4 在 7,8,9 宫，反推得 4789。
    """
    mapping = {
        6: [1, 2, 3],
        4: [7, 8, 9],
    }
    if generating_number not in mapping:
        return []
    poles = mapping[generating_number]
    return [sorted(poles + [generating_number])]


if __name__ == "__main__":
    import json

    result = prune_candidates(1, [6, 7, 8, 9])
    print(json.dumps(result, ensure_ascii=False, indent=2))
