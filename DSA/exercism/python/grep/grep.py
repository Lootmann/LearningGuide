import re
from typing import List


def parse(flags: str) -> List[str]:
    return flags.split(" ")


def read_text(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()


class Formatter:
    def __init__(self, options: List[str], need_filename: bool) -> None:
        self.is_linenumber = False
        self.is_filename = False

        if "-n" in options:
            self.is_linenumber = True

        if need_filename:
            self.is_filename = True

    def formatting(self, text: str, num: int, filename: str) -> str:
        result = []

        if self.is_filename:
            result.append(filename)

        if self.is_linenumber:
            result.append(str(num))

        result.append(text.strip())

        return ":".join(result) + "\n"


def grep(pattern: str, flags: str, files: list) -> str:
    """
    -n : linnumber
    -i : ignore case
    -l : show only filenames
    """
    options = parse(flags)
    format = Formatter(options, len(files) > 1)

    compile = re.compile(pattern)
    if "-i" in options:
        compile = re.compile(pattern, re.IGNORECASE)

    result = []

    if flags == "":
        for filename in files:
            text = read_text(filename).strip()

            for line in text.split("\n"):
                if compile.search(line):
                    result.append(format.formatting(line, 0, filename))
        else:
            return "".join(result)

    if "-l" in options:
        for filename in files:
            text = read_text(filename)

            if re.findall(pattern, text) != []:
                result.append(filename + "\n")
        else:
            return "".join(result)

    if "-n" in options:
        for filename in files:
            text = read_text(filename).strip()

            for linenumber, line in enumerate(text.split("\n")):
                if compile.search(line):
                    result.append(format.formatting(line, linenumber + 1, filename))
        else:
            return "".join(result)

    if "-v" in options:
        for filename in files:
            text = read_text(filename).strip()

            for linenumber, line in enumerate(text.split("\n")):
                if "-x" in options:
                    if not compile.search(line):
                        result.append(format.formatting(line, linenumber + 1, filename))
                else:
                    if not compile.search(line):
                        result.append(format.formatting(line, linenumber + 1, filename))

        else:
            return "".join(result)

    if "-x" in options:
        for filename in files:
            text = read_text(filename)
            for linenumber, row in enumerate(text.split("\n")):
                if compile.match(row):
                    result.append(format.formatting(row, linenumber + 1, filename))
        else:
            return "".join(result)

    for filename in files:
        text = read_text(filename)
        for linenumber, row in enumerate(text.split("\n")):
            if compile.search(row):
                result.append(format.formatting(row, linenumber + 1, filename))
    else:
        return "".join(result)

    return "boom"
