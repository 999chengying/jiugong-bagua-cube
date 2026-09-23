# -*- coding: utf-8 -*-
"""二十四山循环分析。"""

import math
import os
import sys
from itertools import combinations

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from jiugong_encoder import classify_tetra

MOUNTAINS = [
    {"name": "子", "palace": 1, "number": 7},
    {"name": "癸", "palace": 1, "number": 8},
    {"name": "丑", "palace": 8, "number": 3},
    {"name": "艮", "palace": 8, "number": 4},
    {"name": "寅", "palace": 8, "number": 2},
    {"name": "甲", "palace": 3, "number": 8},
    {"name": "卯", "palace": 3, "number": 7},
    {"name": "乙", "palace": 3, "number": 6},
    {"name": "辰", "palace": 4, "number": 6},
    {"name": "巽", "palace": 4, "number": 8},
    {"name": "巳", "palace": 4, "number": 7},
    {"name": "丙", "palace": 9, "number": 4},
    {"name": "午", "palace": 9, "number": 3},
    {"name": "丁", "palace": 9, "number": 2},
    {"name": "未", "palace": 2, "number": 7},
    {"name": "坤", "palace": 2, "number": 6},
    {"name": "申", "palace": 2, "number": 8},
    {"name": "庚", "palace": 7, "number": 2},
    {"name": "酉", "palace": 7, "number": 3},
    {"name": "辛", "palace": 7, "number": 4},
    {"name": "戌", "palace": 6, "number": 4},
    {"name": "乾", "palace": 6, "number": 2},
    {"name": "亥", "palace": 6, "number": 3},
    {"name": "壬", "palace": 1, "number": 6},
]

FORM_PRIORITY = {"生": 5, "化": 4, "变": 3, "恒": 2, "空": 1, "未知": 0}


def _priority(form):
    return FORM_PRIORITY.get(form, 0)


def classify_palace_set(palaces):
    unique = sorted(set(palaces))
    if len(unique) < 3:
        return {"form": "无效", "volume": None, "numbers": unique}
    if len(unique) == 3:
        return {"form": "空", "volume": 0.0, "numbers": unique, "note": "三点共面"}

    candidates = []
    if 1 in unique and 9 in unique:
        candidates.append([x for x in unique if x != 1])
        candidates.append([x for x in unique if x != 9])
    elif 1 in unique:
        candidates.append([x for x in unique if x != 1])
    elif 9 in unique:
        candidates.append([x for x in unique if x != 9])
    else:
        candidates.append(unique)

    expanded = []
    for c in candidates:
        if len(c) == 3:
            expanded.append(c)
        elif len(c) == 4:
            expanded.append(c)
        elif len(c) > 4:
            expanded.extend([list(comb) for comb in combinations(c, 4)])

    best = None
    for c in expanded:
        if len(c) == 3:
            r = {"form": "空", "volume": 0.0, "numbers": c, "note": "三点共面"}
        elif len(c) == 4:
            r = classify_tetra(c)
        else:
            continue
        if not r.get("valid") and r.get("form") != "空":
            continue
        p = _priority(r.get("form"))
        if best is None or p > best[0]:
            best = (p, r)

    if best:
        return best[1]
    return {"form": "未知", "volume": None, "numbers": unique}


def analyze_cycle(K, start_name="子"):
    if K <= 0:
        raise ValueError("K必须为正整数")
    names = [m["name"] for m in MOUNTAINS]
    if start_name not in names:
        raise ValueError("起点必须是二十四山之一：" + ",".join(names))

    start_idx = names.index(start_name)
    g = math.gcd(24, K)
    segments = 24 // g
    circles = K // g

    segs = []
    for n in range(segments):
        idx = (start_idx + n * K) % 24
        m = MOUNTAINS[idx]
        cumulative = n * K
        circle = cumulative // 24
        segs.append({
            "segment": n,
            "cumulative_steps": cumulative,
            "circle": circle,
            "mountain": m["name"],
            "palace": m["palace"],
            "number": m["number"],
        })

    groups = {}
    for s in segs:
        groups.setdefault(s["circle"], []).append(s)

    circles_out = []
    for c in sorted(groups):
        segs_c = groups[c]
        palaces = [s["palace"] for s in segs_c]
        unique = sorted(set(palaces))
        form = classify_palace_set(unique)
        circles_out.append({
            "circle": c,
            "segments": [s["segment"] for s in segs_c],
            "mountains": [s["mountain"] for s in segs_c],
            "palaces": palaces,
            "unique_palaces": unique,
            "form": form.get("form"),
            "form_detail": form,
        })

    return {
        "K": K,
        "start": start_name,
        "gcd": g,
        "segments": segments,
        "circles": circles,
        "segments_detail": segs,
        "circles_detail": circles_out,
    }


if __name__ == "__main__":
    import json

    K = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    start = sys.argv[2] if len(sys.argv) > 2 else "子"
    print(json.dumps(analyze_cycle(K, start), ensure_ascii=False, indent=2))
