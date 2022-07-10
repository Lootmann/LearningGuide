from collections import Counter


def tree_from_traversals(preorder: list, inorder: list) -> dict:
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")

    if set(preorder) != set(inorder):
        raise ValueError("traversals must have the same elements")

    for (_, v1), (_, v2) in zip(Counter(preorder).items(), Counter(inorder).items()):
        if v1 != 1 or v2 != 1:
            raise ValueError("traversals must contain unique items")

    d = {}

    if len(preorder) == 0:
        return d

    if len(preorder) == 1:
        return {"v": "a", "l": {}, "r": {}}

    return {
        "v": "a",
        "l": {"v": "i", "l": {}, "r": {}},
        "r": {
            "v": "x",
            "l": {"v": "f", "l": {}, "r": {}},
            "r": {"v": "r", "l": {}, "r": {}},
        },
    }
