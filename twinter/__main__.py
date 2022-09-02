__all__ = []
__author__ = """whege"""
__date__ = "9/1/2022"
__doc__ = """Enter some text here, bitch"""

from sys import argv

from twinter.client import TwitterClient
from twinter.features import make_features


def twinter_main(username: str):
    """
    Handles calling other functions
    :param username:
    :return:
    """
    with TwitterClient() as t:
        tweets = t.get_tweets(username)

    make_features(tweets)


if __name__ == '__main__':
    try:
        account = argv[1]
    except IndexError:
        raise ValueError("Please provide a Twitter account to query.")
    else:
        twinter_main(account.lstrip("@"))
