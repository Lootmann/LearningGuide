def verse(idx: int) -> list:
    if idx == 0:
        return [
            "No more bottles of beer on the wall, no more bottles of beer.",
            "Go to the store and buy some more, 99 bottles of beer on the wall.",
        ]
    elif idx == 1:
        return [
            "1 bottle of beer on the wall, 1 bottle of beer.",
            "Take it down and pass it around, no more bottles of beer on the wall.",
        ]
    elif idx == 2:
        return [
            "2 bottles of beer on the wall, 2 bottles of beer.",
            "Take one down and pass it around, 1 bottle of beer on the wall.",
        ]
    else:
        return [
            f"{idx} bottles of beer on the wall, {idx} bottles of beer.",
            f"Take one down and pass it around, {idx-1} bottles of beer on the wall.",
        ]


def recite(start: int, take: int = 1) -> list:
    res = []

    for i in range(start, start - take, -1):
        res += verse(i)
        if i != start - take + 1:
            res.append("")

    return res
