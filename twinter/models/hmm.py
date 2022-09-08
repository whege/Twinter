__all__ = ["NaiveHMM"]
__author__ = """whege"""
__date__ = "9/8/2022"
__doc__ = """Text generation using Hidden Markov Models"""

from markovify import NewlineText

from twinter.common.klasses import NeatTweet


def NaiveHMM(tweets: list[NeatTweet]) -> NewlineText:
    """
    Creates a Naive Hidden Markov Model based solely on the corpus of Tweets
    :param tweets: List of NeatTweet objects
    :return: NewlineText model
    """
    return NewlineText("\n".join([str(i) for i in tweets]))
