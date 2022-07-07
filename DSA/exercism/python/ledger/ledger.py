# -*- coding: utf-8 -*-
from datetime import datetime
from pydoc import describe
from typing import List


class LedgerEntry:
    def __init__(self, date: str, description: str, change: int):
        """init

        Args:
            date (str): YYYY-MM-dd
            description (str):
            change (int):
        """
        d = date.split("-")
        self.date = datetime(year=int(d[0]), month=int(d[1]), day=int(d[2]))
        self.description = description
        self.change = change

    def __gt__(self, other: "LedgerEntry") -> bool:
        if self.change > other.change:
            return True
        elif self.change < other.change:
            return False
        return False


def create_entry(date, description, change) -> LedgerEntry:
    return LedgerEntry(date, description, change)


def format_entries(currency, locale, entries: List[LedgerEntry]):
    """format_entries


    :param currency: str - "EUR" or "USD"
    :param locale: str
    :param entries: List[str]
    :return: List[str]
    """
    table = []
    if locale == "en_US":
        table.append("Date       | Description               | Change       ")
    else:
        table.append("Datum      | Omschrijving              | Verandering  ")

    if entries == []:
        return "".join(table)

    row_format = "{:10s} | {:25s} | {:>13s}"
    for entry in sorted(entries):
        datum: str = ""
        changed: str = ""
        description: str = ""

        # datum
        if locale == "en_US":
            datum = "{:02d}/{:02d}/{:04d}".format(
                entry.date.month, entry.date.day, entry.date.year
            )
        else:
            datum = "{:02d}-{:02d}-{:04d}".format(
                entry.date.day, entry.date.month, entry.date.year
            )

        # currenty
        changed = "{:.2f}".format(abs(entry.change) / 100)

        if currency == "USD":
            if locale == "nl_NL":
                if entry.change < 0:
                    changed = (
                        f"$ -{abs(entry.change) // 100},{abs(entry.change) % 100} "
                    )
                else:
                    changed = f"$ {changed[:1]}.{changed[1:].replace('.', ',')} "

            elif len(str(entry.change)) >= 6:
                if abs(entry.change) >= 100000:
                    changed = f"(${changed[:1]},{changed[1:]})"
                else:
                    changed = f"(${changed})"

            elif entry.change >= 0:
                changed = "$" + changed + " "

            else:
                # entry.change < 0
                changed = f"(${changed})"

        else:
            # EUR
            if abs(entry.change) >= 10000:
                changed = f"€ {changed[:1]}.{changed[1:].replace('.', ',')} "
            else:
                changed = f"(€{changed})"

        # description
        description = entry.description
        if len(entry.description) > 25:
            description = entry.description[:22] + "..."

        table.append(
            row_format.format(datum, description, changed),
        )

    return "\n".join(table)
