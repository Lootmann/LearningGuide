""" house.py

Recite the nursery rhyme 'This is the House that Jack Built'.
"""
from typing import List


def recite(start_verse: int, end_verse: int) -> List[str]:
    """recite

    Args:
        start_verse (int):
        end_verse (int):

    Returns:
        List[str]: list of rhymes
    """
    lines = [
        "This is the house that Jack built.",
        "This is the malt that lay in the house that Jack built.",
        "This is the rat that ate the malt that lay in the house that Jack built.",
        "This is the cat that killed the rat that ate the malt that lay in the house that Jack built.",
        "This is the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
        "This is the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
        "This is the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
        "This is the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
        "This is the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
        "This is the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
        "This is the farmer sowing his corn that kept the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
        "This is the horse and the hound and the horn that belonged to the farmer sowing his corn that kept the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
    ]

    start_verse -= 1
    end_verse -= 1
    return lines[start_verse : end_verse + 1]
