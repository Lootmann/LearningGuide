from cli import CLI


def main():
    message = input()
    cli = CLI(message)
    cli.parse()
    print(cli.output())


if __name__ == "__main__":
    main()
