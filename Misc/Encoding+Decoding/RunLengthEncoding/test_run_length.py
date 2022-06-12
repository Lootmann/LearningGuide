from run_length import RunLength


class TestRunoengthEncoding:
    def setup_method(self):
        self.tests = [
            ("A", "A"),
            ("AA", "A2"),
            ("ABCD", "ABCD"),
            ("ABBABB", "AB2AB2"),
            ("AAABBBAAABBB", "A3B3A3B3"),
        ]

        self.tests_long = [
            (
                "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW",
                "W12BW12B3W24BW14",
            ),
            (
                "kwwwwwbbbbbwwwwwbbbbbwwwwwbbbbbwwwwwbbbbbwwwwwbbbbbwwwwwbbbbbwwwwwbbbbbwwwwwbbbbbk",
                "kw5b5w5b5w5b5w5b5w5b5w5b5w5b5w5b5k",
            ),
        ]

    def test_encoding(self):
        for (src, want) in self.tests:
            got = RunLength.encoding(src)
            assert got == want

    def test_encoding_long(self):
        for (src, want) in self.tests_long:
            got = RunLength.encoding(src)
            assert got == want
