# src/sorting.py
def merge_sort(left, right) -> list:
    res = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    while i < len(left):
        res.append(left[i])
        i += 1

    while j < len(right):
        res.append(right[j])
        j += 1

    return res


def merge(lst: list) -> list:
    if len(lst) <= 1:
        return lst

    m = len(lst) // 2
    left = merge(lst[:m])
    right = merge(lst[m:])

    return merge_sort(left, right)
