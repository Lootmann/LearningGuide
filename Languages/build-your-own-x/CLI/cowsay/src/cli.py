# src/cli.py


class CLI:
    WIDTH: int = 80

    def __init__(self, user_input: str = ""):
        self._inputs = user_input

    def parse(self) -> None:
        """parse
        parse splits the received string 'message'.
        Limit the number of characters in a line to about 80 chars.

        Args:
            message: str

        Returns:
            None
        """
        self._result = self.split_inputs(self._inputs)

    def split_inputs(self, inputs: str) -> list:
        lines = []
        splitted = inputs.split(" ")

        word_length = 0
        tmp = []

        for i in range(len(splitted)):
            # word length + white space
            word_length += len(splitted[i]) + 1
            tmp.append(splitted[i])

            if i < len(splitted) - 1:
                if CLI.WIDTH < word_length + len(splitted[i + 1]):
                    lines.append(tmp)
                    tmp = []
                    word_length = 0

        if tmp != []:
            lines.append(tmp)

        return [" ".join(line) for line in lines]

    def _cow(self) -> str:
        return r"""
        \  ^__^
         \ (oo)\_______
           (__)\       )\/\
                ||----w |
                ||     ||"""

    def _white_space(self, string: str) -> str:
        # remove one white space because left_sep needs space
        return " " * (CLI.WIDTH - len(string) - 2)

    def _enclose(self, string: str, left_sep: str, right_sep: str) -> str:
        return "{} {}{}{}\n".format(
            left_sep, string, self._white_space(string), right_sep
        )

    def enclose(self, inputs: list) -> str:
        # get the max length of each string 'result'
        max_length = 0
        for line in inputs:
            max_length = max(max_length, len(line))

        # top
        result = " " + "-" * (CLI.WIDTH - 1) + "\n"

        # online inputs
        if len(inputs) == 1:
            result += self._enclose(inputs[0], "|", "|")
        else:
            result += self._enclose(inputs[0], "/", "\\")

            for i in range(1, len(inputs) - 1):
                result += self._enclose(inputs[i], "|", "|")

            result += self._enclose(inputs[-1], "\\", "/")

        # bottom
        result += " " + "-" * (CLI.WIDTH - 1)

        return result

    def output(self) -> str:
        return self.enclose(self._result) + self._cow()
