def encode(string: str) -> str:
    if string == "":
        return ""

    res = []

    cnt = 1
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            cnt += 1
        else:
            if cnt != 1:
                res.append(str(cnt))
            res.append(string[i])
            cnt = 1

    if cnt != 1:
        res.append(str(cnt))
    res.append(string[-1])

    return "".join(res)


def decode(string: str) -> str:
    if string == "":
        return ""

    res = []
    digit = []
    for ch in string:
        if ch.isdigit():
            digit.append(ch)
        else:
            num = 1 if digit == [] else int("".join(digit))
            res.append(ch * num)
            digit = []

    return "".join(res)
