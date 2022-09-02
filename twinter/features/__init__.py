__all__ = ['make_features']
__author__ = """whege"""
__date__ = "9/2/2022"
__doc__ = """Enter some text here, bitch"""

from typing import List

from twinter.common.klasses import NeatTweet
from .janitor import clean_tweets


def make_features(tweets):
    cleaned_tweets: List[NeatTweet] = clean_tweets(tweets)
    valid_tweets = [tweet for tweet in cleaned_tweets if tweet.neat_text != '']
    print()
