from run_length import RunLength


class TestRunLengthEncoding:
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


class TestRunLengthDecoding:
    def setup_method(self):
        self.tests = [
            ("A", "A"),
            ("A2", "AA"),
            ("ABCD", "ABCD"),
            ("AB2AB2", "ABBABB"),
            ("A3B3A3B3", "AAABBBAAABBB"),
        ]

        self.tests_long = [
            (
                "W12BW12B3W24BW14",
                "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW",
            ),
            (
                "kw5b5w5b5w5b5w5b5w5b5w5b5w5b5w5b5k",
                "kwwwwwbbbbbwwwwwbbbbbwwwwwbbbbbwwwwwbbbbbwwwwwbbbbbwwwwwbbbbbwwwwwbbbbbwwwwwbbbbbk",
            ),
        ]

    def test_decoding(self):
        for (src, want) in self.tests:
            got = RunLength.decoding(src)
            assert got == want

    def test_decoding_long(self):
        for (src, want) in self.tests_long:
            got = RunLength.decoding(src)
            assert got == want
