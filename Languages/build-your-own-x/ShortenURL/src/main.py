"""
src/main.py
"""
from urllib.parse import urlparse

import shorten
from db import DB


def get_user_input() -> str:
    """
    An input is like:      https://www.w3.org
    and this output is like: www.w3.org

    :return: str
    """
    parsed = urlparse(input())
    return parsed.hostname


def main():
    db = DB()
    url = get_user_input()

    if db.find_url(url):
        # TODO: print shorten_url
        print(db.get_shorten_url(url))
        return

    shorten_url = shorten.create_shorten_url()
    db.insert_url(url, shorten_url)
    print(shorten_url)


if __name__ == "__main__":
    main()
