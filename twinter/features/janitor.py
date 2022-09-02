__all__ = ['clean_tweets']
__author__ = """whege"""
__date__ = "9/2/2022"
__doc__ = """Basic cleaning of tweets"""

import re

from twinter.common.klasses import NeatTweet

HANDLE = re.compile(r'@[a-zA-Z0-9_]+(?=\s)')
PUNCT = re.compile(r'[.!,?]')
NEWLINE = re.compile(r'\n+')
UNICODE = re.compile(r'\\U[a-z0-9]+')


def _clean_tweet(tweet: NeatTweet) -> NeatTweet:
    """
    Clean a single tweet
    :param tweet:
    :return:
    """
    # Break the tweet into its word components, normalize unicode characters, then join back together
    text = " ".join([_normalize_unicode(word) for word in tweet.text.split(' ')])
    clean = HANDLE.sub('', text)  # Remove Twitter handles
    clean = re.sub(r'\s+', ' ', clean)  # Remove extra spaces
    clean = NEWLINE.sub(' ', clean)  # Remove newline characters

    # remove punctuation so that we can check if punctuation is all that remains
    punctless = PUNCT.sub('', clean)
    punctless = re.sub(r'\s+', '', punctless)

    # Set neat_text to the empty string if the Tweet is just a handle and/or punctuation, o.w. the cleaned text
    tweet.neat_text = '' if punctless == '' else clean.strip()
    return tweet


def _normalize_unicode(word: str) -> str:
    """
    Normalize unicode characters in a Tweet
    :param word:
    :return:
    """
    if not any(c.isalnum() for c in word):
        return word.encode("unicode_escape").decode().strip()
    else:
        return word


def _unnormalize_unicode(word: str):
    """
    Convert Unicode Character code back to the character
    :param word:
    :return:
    """
    return word.encode().decode("unicode_escape")


def clean_tweets(tweets: list[NeatTweet]) -> list[NeatTweet]:
    """
    Clean a List of Tweets
    :param tweets:
    :return:
    """
    return list(map(_clean_tweet, tweets))
