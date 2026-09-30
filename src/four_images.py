# -*- coding: utf-8 -*-
"""
四象结构：24 老阴、28 少阳、32 少阴、36 老阳。
"""

FOUR_IMAGES = {
    "老阴": {
        "number": 24,
        "structure": "一维三实，中心空",
        "vertices": 24,
        "wuji_centers": 0,
        "yao": "老阴",
        "yin_yang": "阴",
        "age": "老",
    },
    "少阳": {
        "number": 28,
        "structure": "一维三实两虚，四中心",
        "vertices": 24,
        "wuji_centers": 4,
        "yao": "少阳",
        "yin_yang": "阳",
        "age": "少",
    },
    "少阴": {
        "number": 32,
        "structure": "二维四实，中心空",
        "vertices": 32,
        "wuji_centers": 0,
        "yao": "少阴",
        "yin_yang": "阴",
        "age": "少",
    },
    "老阳": {
        "number": 36,
        "structure": "二维四实，四中心",
        "vertices": 32,
        "wuji_centers": 4,
        "yao": "老阳",
        "yin_yang": "阳",
        "age": "老",
    },
}

GENERATION_CHAIN = ["老阴", "少阳", "少阴", "老阳"]


def get_four_images():
    return FOUR_IMAGES


def get_generation_chain():
    return GENERATION_CHAIN


def print_table():
    print("四象结构表")
    print("=" * 70)
    print(f"{'爻象':<6} {'数':>4} {'顶点':>6} {'戊己':>6} {'结构':<20}")
    print("-" * 70)
    for name in GENERATION_CHAIN:
        item = FOUR_IMAGES[name]
        print(
            f"{item['yao']:<6} {item['number']:>4} {item['vertices']:>6} "
            f"{item['wuji_centers']:>6} {item['structure']:<20}"
        )
    print("-" * 70)
    print("生成链：", " -> ".join(GENERATION_CHAIN))


if __name__ == "__main__":
    print_table()
