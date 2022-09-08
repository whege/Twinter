__all__ = []
__author__ = """whege"""
__date__ = "9/1/2022"
__doc__ = """Enter some text here, bitch"""

from sys import argv

from twinter.client import TwitterClient
from twinter.features import make_features
from twinter.common.klasses import NeatTweet


def twinter_main(username: str):
    """
    Handles calling other functions
    :param username:
    :return:
    """
    with TwitterClient() as t:
        tweets = t.get_tweets(username)

    neat_tweets = list(map(NeatTweet, tweets))
    neat_tweets = [t for t in neat_tweets if t.not_empty]
    make_features(neat_tweets)


if __name__ == '__main__':
    try:
        account = argv[1]
    except IndexError:
        raise ValueError("Please provide a Twitter account to query.")
    else:
        twinter_main(account.lstrip("@"))
