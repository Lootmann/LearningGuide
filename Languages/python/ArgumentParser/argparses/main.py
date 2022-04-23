import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("words", nargs="+")
    args = parser.parse_args()

    input_words = " ".join(args.words)
    print(input_words)


if __name__ == "__main__":
    main()
