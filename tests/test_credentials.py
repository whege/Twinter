__all__ = []
__author__ = """whege"""
__date__ = "9/1/2022"
__doc__ = """Enter some text here, bitch"""


from os import environ

import unittest

import tweepy
from dotenv import load_dotenv


class MyTestCase(unittest.TestCase):
    @staticmethod
    def test_something():
        load_dotenv()

        auth = tweepy.OAuth1UserHandler(
            access_token=environ['ACCESS_TOKEN'],
            access_token_secret=environ['ACCESS_TOKEN_SECRET'],
            consumer_key=environ['API_KEY'],
            consumer_secret=environ['API_KEY_SECRET']
        )

        api = tweepy.API(auth)

        public_tweets = api.home_timeline()
        for tweet in public_tweets:
            print(tweet.text)


if __name__ == '__main__':
    unittest.main()
