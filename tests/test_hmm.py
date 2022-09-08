import unittest

from twinter.client import TwitterClient
from twinter.common.klasses import NeatTweet
from twinter.models.hmm import NaiveHMM


class MyTestCase(unittest.TestCase):
    @staticmethod
    def test_something():
        with TwitterClient() as t:
            tweets = t.get_tweets("elonmusk")

        neat_tweets = list(map(NeatTweet, tweets))
        neat_tweets = [t for t in neat_tweets if t.not_empty]

        model = NaiveHMM(neat_tweets)
        while True:
            print(model.make_short_sentence(max_chars=280, max_overlap_ratio=0.5))
            input()


if __name__ == '__main__':
    unittest.main()
