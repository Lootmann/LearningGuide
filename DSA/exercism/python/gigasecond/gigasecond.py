""" gigasecond.py

Given a moment,
determine the moment that would be after a gigasecond has passed.
"""
from datetime import datetime, timedelta


def add(moment: datetime) -> datetime:
    """add

    :param moment: datetime
    :return: datetime - moment + 10^9 seconds
    """
    return moment + timedelta(seconds=10**9)
