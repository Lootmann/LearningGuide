OPTIONS = {}


def register_option(name):
    return OPTIONS.setdefault(name, 1 << len(OPTIONS))


def has_option(options, name):
    return bool(options & name)


def main():
    BLUE = register_option("BLUE")
    RED = register_option("RED")
    WHITE = register_option("WHITE")

    SET = BLUE | RED
    print(has_option(SET, BLUE))
    print(has_option(SET, WHITE))


if __name__ == "__main__":
    main()
