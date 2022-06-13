"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (
    ALCOHOLS,
    KETO,
    OMNIVORE,
    PALEO,
    SPECIAL_INGREDIENTS,
    VEGAN,
    VEGETARIAN,
)


def clean_ingredients(dish_name: str, dish_ingredients: list) -> tuple:
    """Remove duplicates from `dish_ingredients`.

    :param dish_name: str - containing the dish name.
    :param dish_ingredients: list - dish ingredients.
    :return: tuple - containing (dish_name, ingredient set).

    This function should return a `tuple` with the name of the dish as the first item,
    followed by the de-duped `set` of ingredients as the second item.
    """
    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name: str, drink_ingredients: list) -> str:
    """Append "Cocktail" (alcohol)  or "Mocktail" (no alcohol) to `drink_name`,
    based on `drink_ingredients`.

    :param drink_name: str - name of the drink.
    :param drink_ingredients: list - ingredients in the drink.
    :return: str - drink_name appended with "Mocktail" or "Cocktail".

    The function should return the name of the drink followed by "Mocktail" (non-alcoholic)
    and drink name followed by "Cocktail" (includes alcohol).
    """
    for ingredient in drink_ingredients:
        if ingredient in ALCOHOLS:
            return f"{drink_name} Cocktail"
    return f"{drink_name} Mocktail"


def categorize_dish(dish_name: str, dish_ingredients: list) -> str:
    """Categorize `dish_name` based on `dish_ingredients`.

    :param dish_name: str - dish to be categorized.
    :param dish_ingredients: list - ingredients for the dish.
    :return: str - the dish name appended with ": <CATEGORY>".

    This function should return a string with the `dish name: <CATEGORY>` (which meal category the dish belongs to).
    `<CATEGORY>` can be any one of  (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).
    All dishes will "fit" into one of the categories imported from `sets_categories_data.py`
    """
    set_gredient = set(dish_ingredients)

    if set_gredient <= VEGAN:
        return f"{dish_name}: VEGAN"
    if set_gredient <= VEGETARIAN:
        return f"{dish_name}: VEGETARIAN"
    if set_gredient <= PALEO:
        return f"{dish_name}: PALEO"
    if set_gredient <= KETO:
        return f"{dish_name}: KETO"
    if set_gredient <= OMNIVORE:
        return f"{dish_name}: OMNIVORE"

    return "hoge"


def tag_special_ingredients(dish: list) -> tuple:
    """Compare `dish` ingredients to `SPECIAL_INGREDIENTS`.

    :param dish: list - of (dish name, list of dish ingredients).
    :return: tuple - containing (dish name, dish special ingredients).

    Return the dish name followed by the `set` of ingredients that require a special note on the dish description.
    For the purposes of this exercise, all allergens or special ingredients that need to be tracked are in the
    SPECIAL_INGREDIENTS constant imported from `sets_categories_data.py`.
    """
    specials = set()

    for gredient in dish[1]:
        if gredient in SPECIAL_INGREDIENTS:
            specials.add(gredient)

    return (dish[0], specials)


def compile_ingredients(dishes: list) -> set:
    """Create a master list of ingredients.

    :param dishes: list - of dish ingredient sets.
    :return: set - of ingredients compiled from `dishes`.

    This function should return a `set` of all ingredients from all listed dishes.
    """
    compiled = set()

    for dish in dishes:
        compiled |= dish

    return compiled


def separate_appetizers(dishes: list, appetizers: list) -> list:
    """Determine which `dishes` are designated `appetizers` and remove them.

    :param dishes: list - of dish names.
    :param appetizers: list - of appetizer names.
    :return: list - of dish names that do not appear on appetizer list.

    The function should return the list of dish names with appetizer names removed.
    Either list could contain duplicates and may require de-duping.
    """
    return list(set(dishes) ^ set(appetizers))


def singleton_ingredients(dishes: list, intersection: set) -> set:
    """Determine which `dishes` have a singleton ingredient (an ingredient that only appears once across dishes).

    :param dishes: list - of ingredient sets.
    :param intersection: constant - can be one of `<CATEGORY>_INTERSECTION` constants imported from `sets_categories_data.py`.
    :return: set - containing singleton ingredients.

    Each dish is represented by a `set` of its ingredients.

    Each `<CATEGORY>_INTERSECTION` is an `intersection` of all dishes in the category. `<CATEGORY>` can be any one of:
        (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).

    The function should return a `set` of ingredients that only appear in a single dish.
    """
    singles = set()

    for dish in dishes:
        singles ^= dish

    return singles - intersection
