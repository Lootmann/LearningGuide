def transpose(lines) -> str:
    if not lines:
        return ""

    lines = lines.split("\n")
    length = max(len(line) for line in lines)

    res = []

    for i, line in enumerate(lines):
        row = []

        for s in line:
            row.append(s)

        if i == 0:
            for j in range(length):
                if len(row) > j:
                    res.append(row[j])
                else:
                    res.append(" ")
        else:
            for j in range(length):
                if len(row) > j:
                    res[j] += row[j]
                else:
                    res[j] += " "

    # count white spaces
    widths = [0 for _ in range(length)]
    max_length = 0

    for line in reversed(lines):
        max_length = max(max_length, len(line))
        for i in range(max_length):
            widths[i] += 1

    # strip
    for i in range(len(res)):
        res[i] = res[i][: widths[i]]

    return "\n".join(res)
