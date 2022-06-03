from src.cli import CLI

test_strings = {
    "blank": "",
    "wow": "wow",
    "short": "Why hello friends :^) How are you doin?",
    "words": "a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z",
    "80": "0123456789 0123456789 0123456789 0123456789 0123456789 0123456789 0123456789 0123456789",
    "81": "0123456789 0123456789 0123456789 0123456789 0123456789 0123456789 0123456789 0123456789 0",
}


class TestSplitMessage:
    def setup_method(self):
        self.cli = CLI()

    def test_blank(self):
        want = ["wowo"]
        got = self.cli.split_inputs("wowo")
        assert want == got

    def test_short_msg(self):
        want = [test_strings["short"]]
        got = self.cli.split_inputs(test_strings["short"])
        assert want == got

    def test_words(self):
        want = [
            "a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n",
            "o p q r s t u v w x y z",
        ]
        got = self.cli.split_inputs(test_strings["words"])
        assert want == got

    def test_just_80_length(self):
        want = [
            "0123456789 0123456789 0123456789 0123456789 "
            "0123456789 0123456789 0123456789",
            "0123456789",
        ]
        got = self.cli.split_inputs(test_strings["80"])
        assert want == got

    def test_just_81_length(self):
        want = [
            "0123456789 0123456789 0123456789 0123456789 "
            "0123456789 0123456789 0123456789",
            "0123456789 0",
        ]
        got = self.cli.split_inputs(test_strings["81"])
        assert want == got


class TestEnclose:
    def setup_method(self):
        self.cli = CLI()

    def test_hello(self):
        got = self.cli.enclose(["hello"])
        want = ""
        want += " -------------------------------------------------------------------------------\n"
        want += "| hello                                                                         |\n"
        want += " -------------------------------------------------------------------------------"

        assert got == want

    def test_short(self):
        got = self.cli.enclose([test_strings["short"]])
        want = ""
        want += " -------------------------------------------------------------------------------\n"
        want += "| Why hello friends :^) How are you doin?                                       |\n"
        want += " -------------------------------------------------------------------------------"

        assert got == want
