"""
src/main.py
"""
from src import cache, shorten


def get_user_input() -> str:
    """
    An input is like:
        https://www.w3.org

    and an output is like:
        www.w3.org

    :return: str
    """
    return input()


def main():
    cache.init_db()

    url = get_user_input()

    if cache.find_url(url):
        print(cache.get_shorten_url(url))
        return

    shorten_url = shorten.create_shorten_url(url)
    cache.create_cache(url, shorten_url)
    print(shorten_url)


if __name__ == "__main__":
    main()
