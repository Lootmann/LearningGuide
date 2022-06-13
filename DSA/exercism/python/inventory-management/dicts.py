"""Functions to keep track and alter inventory."""
from collections import defaultdict
from typing import DefaultDict, Dict, List, Tuple


def create_inventory(items: List[str]) -> DefaultDict:
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    inventory = defaultdict(int)

    for item in items:
        inventory[item] += 1

    return inventory


def add_items(inventory: Dict, items: List[str]):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1

    return inventory


def decrement_items(inventory: Dict, items: List[str]) -> dict:
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    for item in items:
        if item in inventory:
            inventory[item] = max(inventory[item] - 1, 0)

    return inventory


def remove_item(inventory: Dict, item: List[str]) -> Dict:
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    inventory.pop(item, None)
    return inventory


def list_inventory(inventory: dict) -> List[Tuple[str, int]]:
    """Create a list containing all (item_name, item_count) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    lists = []
    for item, cost in inventory.items():
        if cost > 0:
            lists.append((item, cost))
    return lists
