""" leap.py
Given a year, report if it is a leap year.
"""


def leap_year(year: int) -> bool:
    """leap_year

    if year % 400 == 0:
        return True

    if year % 4 == 0 and year % 100 != 0:
        return True

    return False

    :param year: int - a year
    :return: return True when 'year' is leap year
    """
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
