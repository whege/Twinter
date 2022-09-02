__all__ = ["NeatTweet"]
__author__ = """whege"""
__date__ = "9/2/2022"
__doc__ = """Enter some text here, bitch"""

from typing import Union

from tweepy import Tweet


class NeatTweet(Tweet):
    def __init__(self, data: Union[dict, Tweet]):
        if isinstance(data, dict):
            super(NeatTweet, self).__init__(data=data)
        elif isinstance(data, Tweet):
            super(NeatTweet, self).__init__(data=data.data)
        else:
            raise TypeError

        self._neat_text = None

    @property
    def neat_text(self) -> str:
        return self._neat_text

    @neat_text.setter
    def neat_text(self, other: str) -> None:
        if not isinstance(other, str):
            raise ValueError
        else:
            self._neat_text = other
