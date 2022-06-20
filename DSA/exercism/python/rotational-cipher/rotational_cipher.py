def conv(ch: str, key: int, const: int) -> str:
    return chr(((ord(ch) - const + key) % 26) + const)


def rotate(text: str, key: int) -> str:
    """rotate
    Caesar Cypher

    :param text: str - plain text
    :return: int
    """
    cypher = []

    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                cypher.append(conv(ch, key, ord("A")))
            else:
                cypher.append(conv(ch, key, ord("a")))
        else:
            cypher.append(ch)

    return "".join(cypher)
