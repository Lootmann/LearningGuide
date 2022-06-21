from collections import defaultdict
import re


def count_words(sentence: str) -> dict:
    res = defaultdict(int)

    sentence = re.sub(r"[,.:_!@$%&\^]", " ", sentence)

    for word in sentence.split():
        w = word.strip("'").lower()

        if w != "":
            res[w] += 1

    print(res)

    return dict(res)
