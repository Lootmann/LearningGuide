# test.py
from base64 import Base64
import unittest


class TestBase64Encoding_ch_to_bit(unittest.TestCase):
    def test_1(self):
        got = Base64.ch_to_bit("A")
        want = "01000001"
        self.assertEqual(got, want)

    def test_2(self):
        got = Base64.ch_to_bit("Z")
        want = "01011010"
        self.assertEqual(got, want)


class TestBase64Encoding_split(unittest.TestCase):
    def test_split(self):
        string = "ABCDEFG"
        got = Base64.split(string)
        want = [
            "010000",
            "010100",
            "001001",
            "000011",
            "010001",
            "000100",
            "010101",
            "000110",
            "010001",
            "110000",
        ]
        self.assertEqual(got, want)


class TestBase64Encoding_encode(unittest.TestCase):
    def test_encode(self):
        got = Base64.encode("ABCDEFG")
        want = "QUJDREVGRw=="
        self.assertEqual(got, want)

    def test_encode1(self):
        got = Base64.encode("abcdefg")
        want = "YWJjZGVmZw=="
        self.assertEqual(got, want)

    def test_encode2(self):
        got = Base64.encode("ukraine")
        want = "dWtyYWluZQ=="
        self.assertEqual(got, want)

    def test_encode3(self):
        got = Base64.encode("AgainstTheDestiny")
        want = "QWdhaW5zdFRoZURlc3Rpbnk="
        self.assertEqual(got, want)


if __name__ == "__main__":
    unittest.main()
