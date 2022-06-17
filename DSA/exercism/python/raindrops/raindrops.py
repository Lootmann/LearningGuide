def convert(number: int) -> str:
    result = []

    mods = [(3, "Pling"), (5, "Plang"), (7, "Plong")]

    for mod, drop in mods:
        if number % mod == 0:
            result.append(drop)

    if result == []:
        return str(number)

    return "".join(result)
