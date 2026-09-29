# -*- coding: utf-8 -*-
"""
九宫八卦立方体 benchmark 脚本
对比 A 组（自由推理）与 B 组（结构查表）的字符数（token 代理）。
"""

import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(BASE_DIR, "src")
sys.path.insert(0, SRC_DIR)

from jiugong_encoder import classify_tetra
from cycle_analysis import analyze_cycle

TEST_CASES = [
    {"type": "tetra", "numbers": [1, 6, 7, 8], "desc": "坤1宫生形"},
    {"type": "tetra", "numbers": [1, 3, 6, 8], "desc": "表面共面空形"},
    {"type": "tetra", "numbers": [3, 6, 9, 2], "desc": "正四面体3692"},
    {"type": "tetra", "numbers": [1, 4, 7, 8], "desc": "正四面体8147"},
    {"type": "tetra", "numbers": [2, 3, 4, 6], "desc": "变形2346"},
    {"type": "tetra", "numbers": [1, 2, 4, 7], "desc": "生形1247阴径"},
    {"type": "cycle", "K": 5, "start": "子", "desc": "K=5回文"},
    {"type": "cycle", "K": 6, "start": "子", "desc": "K=6四正御街"},
    {"type": "cycle", "K": 6, "start": "未", "desc": "K=6四维御街"},
    {"type": "cycle", "K": 9, "start": "子", "desc": "K=9双恒"},
]


def estimate_a_tokens(case):
    """模拟 A 组自由推理的文本长度（字符数）。"""
    if case["type"] == "tetra":
        nums = case["numbers"]
        text = (
            f"我们来分析数字 {nums} 的几何形态。"
            "首先，将每个数字映射到立方体坐标："
            "乾9(0,0,0)、兑4(1,0,0)、离3(1,1,0)、震8(0,1,0)、"
            "巽2(1,0,1)、坎7(0,0,1)、艮6(0,1,1)、坤1(1,1,1)。"
            f"然后计算这四个点 {nums} 两两之间的距离平方，得到六条棱长。"
            "根据棱长多重集判断形态："
            "如果全是2则为恒；如果1,1,1,2,2,2则为生；"
            "如果1,1,1,2,2,3则为化；如果1,1,2,2,2,3则为变；"
            "如果四点共面则为空。"
            "经过仔细计算，我们得到结论。"
        )
        return len(text)
    elif case["type"] == "cycle":
        K = case["K"]
        start = case["start"]
        text = (
            f"我们来分析步长 K={K}，起点为 {start} 的二十四山循环。"
            "首先列出二十四山圆序，然后每隔 K 步取一个起点，计算段数和圈数。"
            "接着根据每圈包含的宫数，判断其几何形态。"
            "最后汇总各圈形态。"
        )
        return len(text)
    return 0


def estimate_b_tokens(case):
    """调用结构编码器，统计输出字符数。"""
    if case["type"] == "tetra":
        result = classify_tetra(case["numbers"])
        out = {"form": result["form"], "volume": result["volume"]}
        return len(json.dumps(out, ensure_ascii=False))
    elif case["type"] == "cycle":
        result = analyze_cycle(case["K"], case["start"])
        out = {
            "K": result["K"],
            "segments": result["segments"],
            "circles": result["circles"],
            "forms": [c["form"] for c in result["circles_detail"]],
        }
        return len(json.dumps(out, ensure_ascii=False))
    return 0


def main():
    print("九宫八卦立方体 Benchmark v2.1")
    print("=" * 60)
    print(f"{'用例':<30} {'A组字符':>10} {'B组字符':>10} {'节省':>10}")
    print("-" * 60)
    total_a = 0
    total_b = 0
    for case in TEST_CASES:
        a = estimate_a_tokens(case)
        b = estimate_b_tokens(case)
        total_a += a
        total_b += b
        save = (a - b) / a * 100 if a > 0 else 0
        print(f"{case['desc']:<30} {a:>10} {b:>10} {save:>9.1f}%")
    print("-" * 60)
    save_total = (total_a - total_b) / total_a * 100 if total_a > 0 else 0
    print(f"{'总计':<30} {total_a:>10} {total_b:>10} {save_total:>9.1f}%")
    print()
    print("注意：字符数仅为 token 的粗略代理，真实 token 需接入模型后测量。")


if __name__ == "__main__":
    main()
