# src/main.py
import cli
from db import DB


def main():
    db = DB()
    db.insert(weight=73.00, fat_rate=20.00)

    cli.cli()

    db.dump()


if __name__ == "__main__":
    main()
