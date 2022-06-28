def verbs(idx: int) -> list:
    idx -= 1

    if idx == 0:
        return [
            "I know an old lady who swallowed a fly.",
            "I don't know why she swallowed the fly. Perhaps she'll die.",
        ]
    elif idx == 1:
        return [
            "I know an old lady who swallowed a spider.",
            "It wriggled and jiggled and tickled inside her.",
            "She swallowed the spider to catch the fly.",
            "I don't know why she swallowed the fly. Perhaps she'll die.",
        ]

    elif idx == 2:
        return [
            "I know an old lady who swallowed a bird.",
            "How absurd to swallow a bird!",
            "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.",
            "She swallowed the spider to catch the fly.",
            "I don't know why she swallowed the fly. Perhaps she'll die.",
        ]
    elif idx == 3:
        return [
            "I know an old lady who swallowed a cat.",
            "Imagine that, to swallow a cat!",
            "She swallowed the cat to catch the bird.",
            "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.",
            "She swallowed the spider to catch the fly.",
            "I don't know why she swallowed the fly. Perhaps she'll die.",
        ]
    elif idx == 4:
        return [
            "I know an old lady who swallowed a dog.",
            "What a hog, to swallow a dog!",
            "She swallowed the dog to catch the cat.",
            "She swallowed the cat to catch the bird.",
            "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.",
            "She swallowed the spider to catch the fly.",
            "I don't know why she swallowed the fly. Perhaps she'll die.",
        ]
    elif idx == 5:
        return [
            "I know an old lady who swallowed a goat.",
            "Just opened her throat and swallowed a goat!",
            "She swallowed the goat to catch the dog.",
            "She swallowed the dog to catch the cat.",
            "She swallowed the cat to catch the bird.",
            "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.",
            "She swallowed the spider to catch the fly.",
            "I don't know why she swallowed the fly. Perhaps she'll die.",
        ]
    elif idx == 6:
        return [
            "I know an old lady who swallowed a cow.",
            "I don't know how she swallowed a cow!",
            "She swallowed the cow to catch the goat.",
            "She swallowed the goat to catch the dog.",
            "She swallowed the dog to catch the cat.",
            "She swallowed the cat to catch the bird.",
            "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.",
            "She swallowed the spider to catch the fly.",
            "I don't know why she swallowed the fly. Perhaps she'll die.",
        ]
    elif idx == 7:
        return [
            "I know an old lady who swallowed a horse.",
            "She's dead, of course!",
        ]
    else:
        return ["boom"]


def recite(start_verse: int, end_verse: int) -> list:
    """recite

    :param start_verse: int
    :param end_verse: int
    :return: list
    """
    res = []

    if start_verse == end_verse:
        return verbs(start_verse)

    for i in range(start_verse, end_verse + 1):
        res += verbs(i)
        if i != end_verse:
            res.append("")

    for line in res:
        print(line)

    return res
