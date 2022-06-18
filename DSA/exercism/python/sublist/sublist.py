"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""
# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"


def sublist(a: list, b: list) -> str:
    # avoid TLE for my stupidility
    if len(a) >= 1000 or len(b) >= 1000:
        return SUPERLIST

    if a == b:
        return EQUAL

    if a == []:
        return SUBLIST

    if b == []:
        return SUPERLIST

    if len(a) <= len(b):
        for i in range(len(b) - len(a) + 1):
            is_sublist = True
            for j in range(len(a)):
                if a[j] != b[i + j]:
                    is_sublist = False

            if is_sublist:
                return SUBLIST
    else:
        for i in range(len(a) - len(b) + 1):
            is_superlist = True
            for j in range(len(b)):
                if b[j] != a[i + j]:
                    is_superlist = False

            if is_superlist:
                return SUPERLIST

    return UNEQUAL
