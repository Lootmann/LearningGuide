"""
src/shorten.py
"""
import random
import string

from src import cache


def create_shorten_url(url: str) -> str:
    """create_shorten_url

    create unique shorten url using random string

    :param url: stripped url (www.w3.org)
    :return: unique random string
    """
    size = 7

    while True:
        # NOTE: completely random string
        rand_string = "".join(random.sample(list(string.ascii_letters), size))
        if not cache.find_shorten_url(rand_string):
            return rand_string
