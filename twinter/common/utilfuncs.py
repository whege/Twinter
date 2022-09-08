__all__ = [
    "emojify"
]
__author__ = """whege"""
__date__ = "9/8/2022"
__doc__ = """Utility functions"""


def emojify(word: str):
    """
    Convert Unicode Character code back to the character
    :param word:
    :return:
    """
    return word.encode().decode("unicode_escape")
