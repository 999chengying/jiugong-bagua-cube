# -*- coding: utf-8 -*-
"""九宫八卦立方体编码器。"""

from itertools import combinations

COORDS = {
    9: (0, 0, 0),
    4: (1, 0, 0),
    3: (1, 1, 0),
    8: (0, 1, 0),
    2: (1, 0, 1),
    7: (0, 0, 1),
    6: (0, 1, 1),
    1: (1, 1, 1),
}

FACES = [
    {1, 2, 3, 4},
    {6, 7, 8, 9},
    {1, 3, 6, 8},
    {2, 4, 7, 9},
    {1, 2, 6, 7},
    {3, 4, 8, 9},
]

DIAG_SECTIONS = [
    {1, 3, 7, 9},
    {2, 4, 6, 8},
    {1, 2, 8, 9},
    {3, 4, 6, 7},
    {1, 4, 6, 9},
    {2, 3, 7, 8},
]

GENERATING_PAIRS = [(1, 6), (2, 7), (3, 8), (4, 9)]
DIAGONAL_PAIRS = [(1, 9), (2, 8), (3, 7), (4, 6)]

FORM_VOLUME = {
    "生": 1.0 / 6.0,
    "化": 1.0 / 6.0,
    "变": 1.0 / 6.0,
    "恒": 1.0 / 3.0,
    "空": 0.0,
    "未知": None,
}


def dist_sq(a, b):
    pa = COORDS[a]
    pb = COORDS[b]
    return sum((x - y) ** 2 for x, y in zip(pa, pb))


def classify_tetra(numbers):
    nums = list(numbers)
    result = {
        "valid": False,
        "numbers": nums,
        "coplanar": False,
        "coplanar_type": None,
        "form": "未知",
        "volume": None,
        "generating_pairs": [],
        "diagonal_pairs": [],
        "dist_sq": [],
    }

    if len(nums) != 4:
        result["reason"] = "必须输入四个数字"
        return result
    if len(set(nums)) != 4:
        result["reason"] = "四个数字不能重复"
        return result
    if 5 in nums:
        result["reason"] = "中宫5不参与顶点"
        return result
    if any(n not in COORDS for n in nums):
        result["reason"] = "数字必须在1-9且不含5"
        return result

    result["valid"] = True
    s = set(nums)

    if s in FACES:
        result.update({
            "coplanar": True,
            "coplanar_type": "表面",
            "form": "空",
            "volume": 0.0,
        })
        return result
    if s in DIAG_SECTIONS:
        result.update({
            "coplanar": True,
            "coplanar_type": "对角截面",
            "form": "空",
            "volume": 0.0,
        })
        return result

    ds = sorted(dist_sq(a, b) for a, b in combinations(nums, 2))
    result["dist_sq"] = ds

    if ds == [1, 1, 1, 2, 2, 2]:
        form = "生"
    elif ds == [1, 1, 1, 2, 2, 3]:
        form = "化"
    elif ds == [1, 1, 2, 2, 2, 3]:
        form = "变"
    elif ds == [2, 2, 2, 2, 2, 2]:
        form = "恒"
    else:
        form = "未知"

    result["form"] = form
    result["volume"] = FORM_VOLUME.get(form)

    result["generating_pairs"] = [
        [a, b] for a, b in GENERATING_PAIRS if a in s and b in s
    ]
    result["diagonal_pairs"] = [
        [a, b] for a, b in DIAGONAL_PAIRS if a in s and b in s
    ]

    return result


def encode(numbers):
    return classify_tetra(numbers)


if __name__ == "__main__":
    import json
    import sys

    if len(sys.argv) == 5:
        nums = [int(x) for x in sys.argv[1:5]]
        print(json.dumps(classify_tetra(nums), ensure_ascii=False, indent=2))
    else:
        print("用法: python jiugong_encoder.py 1 6 7 8")
