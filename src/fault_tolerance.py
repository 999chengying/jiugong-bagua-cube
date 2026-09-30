# -*- coding: utf-8 -*-
"""
递归容错模拟：给定失能宫位，检查路径通断，推断故障点。
"""

PATHS = {
    "四正阳行": [1, 3, 9, 7, 1],
    "四维阴行": [2, 4, 8, 6, 2],
    "连续3阳行": [1, 3, 6, 8, 1],
    "连续3阴行": [2, 4, 7, 9, 2],
    "连续2阳行": [3, 4, 8, 9, 3],
    "连续2阴行": [1, 2, 6, 7, 1],
    "阴功正四面体": [8, 1, 4, 7, 8],
    "中宫感知链": [8, 1, 4, 7, 10],
}


def check_paths(faulty_palace):
    """
    检查所有路径是否包含故障宫。
    返回：{路径名: {"通": bool, "含故障": bool}}
    """
    result = {}
    for name, path in PATHS.items():
        contains = faulty_palace in path
        result[name] = {
            "通": not contains,
            "含故障": contains,
        }
    return result


def infer_fault(faulty_palace=None, path_status=None):
    """
    根据路径通断模式推断故障点。
    若给定 faulty_palace，则直接返回该点。
    否则根据 path_status 匹配。
    """
    if faulty_palace is not None:
        return faulty_palace

    if path_status is None:
        raise ValueError("必须提供 faulty_palace 或 path_status")

    candidates = []
    for palace in [1, 2, 3, 4, 6, 7, 8, 9]:
        status = check_paths(palace)
        if status == path_status:
            candidates.append(palace)
    return candidates


def print_report(faulty_palace):
    print(f"模拟故障：离{faulty_palace}宫失能" if faulty_palace == 3 else f"模拟故障：{faulty_palace}宫失能")
    print("=" * 60)
    status = check_paths(faulty_palace)
    for name, info in status.items():
        flag = "通" if info["通"] else "断"
        print(f"{name:<12} {flag}")
    print("-" * 60)
    inferred = infer_fault(faulty_palace)
    print(f"中宫推断故障点：{inferred}")


if __name__ == "__main__":
    print_report(3)
