class RunLength:
    def __init__(self):
        pass

    @classmethod
    def encoding(cls, src: str) -> str:
        """
        compression using Run Length Algorithm

        e.g.)
        A -> A
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
