__all__ = ["TwitterClient"]
__author__ = """whege"""
__date__ = "9/1/2022"
__doc__ = """Enter some text here, bitch"""

from os import environ
from typing import List, Optional

from dotenv import load_dotenv
from tqdm import tqdm
from tweepy import Client, Paginator, Tweet


class TwitterClient:
    def __init__(self):
        self._client: Optional[Client] = None

    def connect(self):
        """
        Connect to the Twitter API
        :return:
        """
        load_dotenv()

        self._client = Client(
            access_token=environ['ACCESS_TOKEN'],
            access_token_secret=environ['ACCESS_TOKEN_SECRET'],
            bearer_token=environ['BEARER_TOKEN'],
            consumer_key=environ['API_KEY'],
            consumer_secret=environ['API_KEY_SECRET']
        )

    def get_tweets(self, screen_name: str, /) -> List[Tweet]:
        """
        Get the timeline for the passed screen_name
        :param screen_name: Screen name of the Twitter user for which to fetch tweets
        :return:
        """
        # Validate that the user actually exists
        if (user := self._client.get_user(username=screen_name)).errors:
            raise ValueError(user.errors[0]['detail'])
        else:
            user = user.data.id

        tweets: List[Tweet] = []
        _kwargs = {'id': user, "exclude": ['retweets'], "max_results": 100, "limit": 3300}

        for res in tqdm(
                Paginator(self._client.get_users_tweets, **_kwargs),
                desc="Fetching", unit=" pages of Tweets", colour="blue"
        ):
            tweets.extend(res.data)

        return tweets

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._client = None
