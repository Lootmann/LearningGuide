import operator
from typing import Dict, List


def format_table(rows: List[Dict]) -> List[str]:
    """format_table

    Args:
        d : raw tables

    Returns:
        List[str]: formatted tables
    """
    # sorted
    rows = sorted(rows, key=lambda k: (-k["P"], k["name"]))

    result = ["Team                           | MP |  W |  D |  L |  P"]

    for row in rows:
        result.append(
            "{:30s} |  {} |  {} |  {} |  {} | {:2d}".format(
                row["name"],
                row["M"],
                row["W"],
                row["D"],
                row["L"],
                row["W"] * 3 + row["D"],
            )
        )

    return result


def tally(rows: List[str]) -> List[str]:
    d = {}

    for row in rows:
        left, right, status = row.split(";")

        if left not in d:
            d[left] = {"M": 0, "W": 0, "L": 0, "D": 0}

        if right not in d:
            d[right] = {"M": 0, "W": 0, "L": 0, "D": 0}

        d[left]["M"] += 1
        d[right]["M"] += 1

        if status == "win":
            d[left]["W"] += 1
            d[right]["L"] += 1

        if status == "loss":
            d[left]["L"] += 1
            d[right]["W"] += 1

        if status == "draw":
            d[left]["D"] += 1
            d[right]["D"] += 1

    result = []

    for k, v in d.items():
        v["name"] = k
        v["P"] = 3 * v["W"] + v["D"]
        result.append(v)

    return format_table(result)
