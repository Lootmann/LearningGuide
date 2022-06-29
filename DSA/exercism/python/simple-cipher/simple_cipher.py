class Cipher:
    def __init__(self, key: str = ""):
        if key == "":
            self.key = "aaaaaaaaaa"
        else:
            self.key = key

    def rot(self, i: int, ch: str, direction: int):
        diff = ord(self.key[i % len(self.key)]) - ord("a")
        return chr((ord(ch) - ord("a") + diff * direction + 26) % 26 + ord("a"))

    def encode(self, text: str) -> str:
        if self.key == "":
            return self.key

        return "".join(self.rot(i, ch, +1) for i, ch in enumerate(text))

    def decode(self, text: str):
        if self.key == "":
            return self.key

        return "".join(self.rot(i, ch, -1) for i, ch in enumerate(text))
