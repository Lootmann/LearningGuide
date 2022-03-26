# base64.py
class Base64:
    @staticmethod
    def padding(src: list, pad: str, length: int) -> None:
        """padding
        padding "pad" to last chunk

        Args:
            src: list - pass by reference
            pad: str
            length: int
        Returns:
            None
        """
        if len(src[-1]) % length != 0:
            src[-1] += pad * (length - len(src[-1]) % length)

    @staticmethod
    def ch_to_bit(char: str) -> str:
        """str to 8 bit (ascii code)

        Args:
            char: str - Ascii Code(a-zA-Z0-9+/)
        Returns:
            bits: str
        """
        bit = bin(ord(char))
        return "{:0>8}".format(bit[2:])

    @staticmethod
    def split(string: str) -> list:
        """splitted bit by 6 bits

        Args:
            string: str - bits "10110101..."
        Returns:
            list - ["0100110", "1101001", ...]
        """
        # string to bit and join bits
        concat = "".join([Base64.ch_to_bit(ch) for ch in string])

        # split by 6 bits
        splitted = [concat[i : i + 6] for i in range(0, len(concat), 6)]

        # padding 0 at last chunk
        Base64.padding(splitted, "0", 6)

        return splitted

    @staticmethod
    def convert_table(char: str) -> str:
        """convert table
        bit to char
        """
        return {
            "000000": "A",
            "000001": "B",
            "000010": "C",
            "000011": "D",
            "000100": "E",
            "000101": "F",
            "000110": "G",
            "000111": "H",
            "001000": "I",
            "001001": "J",
            "001010": "K",
            "001011": "L",
            "001100": "M",
            "001101": "N",
            "001110": "O",
            "001111": "P",
            "010000": "Q",
            "010001": "R",
            "010010": "S",
            "010011": "T",
            "010100": "U",
            "010101": "V",
            "010110": "W",
            "010111": "X",
            "011000": "Y",
            "011001": "Z",
            "011010": "a",
            "011011": "b",
            "011100": "c",
            "011101": "d",
            "011110": "e",
            "011111": "f",
            "100000": "g",
            "100001": "h",
            "100010": "i",
            "100011": "j",
            "100100": "k",
            "100101": "l",
            "100110": "m",
            "100111": "n",
            "101000": "o",
            "101001": "p",
            "101010": "q",
            "101011": "r",
            "101100": "s",
            "101101": "t",
            "101110": "u",
            "101111": "v",
            "110000": "w",
            "110001": "x",
            "110010": "y",
            "110011": "z",
            "110100": "0",
            "110101": "1",
            "110110": "2",
            "110111": "3",
            "111000": "4",
            "111001": "5",
            "111010": "6",
            "111011": "7",
            "111100": "8",
            "111101": "9",
            "111110": "+",
            "111111": "/",
        }.get(char, "?")

    @staticmethod
    def encode(phrase: str) -> str:
        """Encode to Base64 format"""
        # bit to Base64 chars
        converted = [Base64.convert_table(ch) for ch in Base64.split(phrase)]

        # concat by 4 chars
        splitted = ["".join(converted[i : i + 4]) for i in range(0, len(converted), 4)]

        # padding "="
        Base64.padding(splitted, "=", 4)

        return "".join(splitted)
