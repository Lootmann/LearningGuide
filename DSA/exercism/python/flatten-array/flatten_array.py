def flatten(iterable: list) -> list:
    """flatten

    Take a nested list and return a single flattened list
    with all values except nil/null.

    :param iterable: list
    :return: list
    """
    res = []

    for iter in iterable:
        # not iter is True when iter == None 'or' iter == 0
        # so iter == None is needed.
        if iter == None:
            pass
        elif type(iter) == list:
            nested = flatten(iter)
            for obj in nested:
                res.append(obj)
        else:
            res.append(iter)

    return res
