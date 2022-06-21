def find(search_list: list, value: int) -> int:
    if search_list == []:
        raise ValueError("value not in array")

    low, high = 0, len(search_list) - 1
    mid = 0

    while low <= high:
        mid = (low + high) // 2
        if search_list[mid] == value:
            return mid

        elif search_list[mid] < value:
            low = mid + 1

        else:
            high = mid - 1

    if low > high:
        raise ValueError("value not in array")

    return 0
