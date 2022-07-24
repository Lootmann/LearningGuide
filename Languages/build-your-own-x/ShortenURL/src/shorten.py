"""
src/shorten.py
"""
import random
import string

from db import DB


def create_shorten_url() -> str:
    """create_shorten_url

    create unique shorten url using random string

    :param :
    :return: unique random string
    """
    size = 7

    while True:
        db = DB()

        # NOTE: completely random string
        rand_string = "".join(random.sample(list(string.ascii_letters), size))
        if not db.find_shorten_url(rand_string):
            return rand_string
