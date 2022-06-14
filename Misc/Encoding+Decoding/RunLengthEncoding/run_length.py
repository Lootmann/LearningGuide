# run_length.py

import re


class RunLength:
    def __init__(self):
        pass

    @classmethod
    def encoding(cls, src: str) -> str:
        """
        compression using Run Length Algorithm

        e.g.) A -> A
        AB -> AB
        AABB -> A2B2
        AABAABA -> A2BA2BA
        AAAAAAAAA -> A9
        AAAAAAAAAA -> A10
        """
        result = []
        cnt = 1

        # O(N)
        for i in range(len(src) - 1):
            if src[i] == src[i + 1]:
                cnt += 1
            else:
                if cnt == 1:
                    result.append(src[i])
                else:
                    result.append(src[i])
                    result.append(str(cnt))
                    cnt = 1

        result.append(src[-1])
        if cnt != 1:
            result.append(str(cnt))

        # O(N) ?
        return "".join(result)

    @classmethod
    def decoding(cls, encoded: str) -> str:
        # ^[0-9][0-9]*
        # first ch is not [0-9], and rest are all digits.
        matched = re.findall(r"\D\d*", encoded)

        result = []
        for match in matched:
            # one char
            if len(match) == 1:
                result.append(match)
            else:
                # A1, B90, C9999, ...
                digit = match[0]
                rep = int(match[1:])
                result.append(digit * rep)

        return "".join(result)
