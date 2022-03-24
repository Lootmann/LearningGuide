# test.py
from base64 import Base64
import unittest


class Testbase64Encode(unittest.TestCase):
    def encode1(self):
        phrase = "abcdefg"
        encoding = Base64.encode(phrase)
        self.assertEqual(encoding, "YWJjZGVmZw==")

    def encode2(self):
        phrase = "ukraine"
        encoding = Base64.encode(phrase)
        self.assertEqual(encoding, "dWtyYWluZQ==")


if __name__ == "__main__":
    unittest.main()
