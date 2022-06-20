"""atbash_cipher.py

Create an implementation of the atbash cipher,
an ancient encryption system created in the Middle East.
"""


def conv(ch: str) -> str:
    return chr(ord("z") - ord(ch) + ord("a"))


def encode(plain_text: str) -> str:
    """encode plain_text

    :param plain_text: str
    :return: str
    """
    cipher = []

    for ch in plain_text:
        if ch == (" ", "."):
            pass
        elif ch.isalpha():
            cipher.append(conv(ch.lower()))
        elif ch.isdigit():
            cipher.append(ch)
        else:
            pass

    cipher, result = "".join(cipher), []

    if len(cipher) > 5:
        for i in range((len(cipher) + 4) // 5):
            result.append(cipher[5 * i : 5 * i + 5])
    else:
        result.append(cipher)

    return " ".join(result)


def decode(ciphered_text: str) -> str:
    """decode ciphered_text

    :param ciphered_text: str
    :return: str
    """
    plain = []
    for ch in ciphered_text:
        if ch == " ":
            pass
        elif ch.isalpha():
            plain.append(conv(ch))
        else:
            plain.append(ch)

    return "".join(plain)
