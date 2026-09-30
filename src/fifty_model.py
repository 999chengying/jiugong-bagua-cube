# -*- coding: utf-8 -*-
"""
大衍之数 50 模型：5 实 4 虚，十字风车布局。
"""

FIFTY_LAYOUT = {
    "中": {"type": "实", "center": 5, "virtual": False},
    "左": {"type": "实", "center": 5, "virtual": False},
    "右": {"type": "实", "center": 5, "virtual": False},
    "前": {"type": "实", "center": 5, "virtual": False},
    "后": {"type": "实", "center": 5, "virtual": False},
    "左中之间": {"type": "虚", "center": None, "virtual": True},
    "右中之间": {"type": "虚", "center": None, "virtual": True},
    "前中之间": {"type": "虚", "center": None, "virtual": True},
    "后中之间": {"type": "虚", "center": None, "virtual": True},
}


def get_layout():
    return FIFTY_LAYOUT


def count_vertices():
    """
    5 实立方体共享后总顶点数。
    简化：5 实 + 4 虚 = 9 宫，顶点数按二维四实或三维六方共享计算。
    """
    return 32


def summary():
    real_count = sum(1 for v in FIFTY_LAYOUT.values() if v["type"] == "实")
    virtual_count = sum(1 for v in FIFTY_LAYOUT.values() if v["type"] == "虚")
    print("大衍之数 50 模型")
    print("=" * 50)
    print(f"实立方体：{real_count}")
    print(f"虚立方体：{virtual_count}")
    print(f"总宫位：{real_count + virtual_count}")
    print(f"共享后顶点数：{count_vertices()}")
    print(f"50 = 5 × 10 = {5 * 10}")
    print()
    print("布局：")
    for name, item in FIFTY_LAYOUT.items():
        center = item["center"] if item["center"] is not None else "空"
        print(f"  {name:<8} {item['type']}  中心={center}")


if __name__ == "__main__":
    summary()
