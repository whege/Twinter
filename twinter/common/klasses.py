__all__ = ["NeatTweet"]
__author__ = """whege"""
__date__ = "9/2/2022"
__doc__ = """Enter some text here, bitch"""

import re
from typing import Union

from tweepy import Tweet

HANDLE = re.compile(r'@[a-zA-Z0-9_]+(?=\s)')
PUNCT = re.compile(r'[.!,?]')
NEWLINE = re.compile(r'\n+')
UNICODE = re.compile(r'\\U[a-z0-9]+')


class NeatTweet(Tweet):
    def __init__(self, data: Union[dict, Tweet]):
        if isinstance(data, dict):
            super(NeatTweet, self).__init__(data=data)
        elif isinstance(data, Tweet):
            super(NeatTweet, self).__init__(data=data.data)
        else:
            raise TypeError

        self._neat_text = self._clean_tweet()

    @property
    def empty(self) -> bool:
        """
        Returns whether the cleaned Tweet is empty
        :return:
        """
        return len(self) == 0

    @property
    def neat_text(self) -> str:
        return self._neat_text

    @neat_text.setter
    def neat_text(self, other: str) -> None:
        if not isinstance(other, str):
            raise ValueError
        else:
            self._neat_text = other

    @property
    def not_empty(self) -> bool:
        """
        Returns whether the cleaned Tweet is the empty string
        :return:
        """
        return len(self) != 0

    def _clean_tweet(self):
        """
        Clean the tweet of handles, punctuation, emoji, etc.
        :return:
        """
        # Break the tweet into its word components, normalize unicode characters, then join back together
        text = " ".join([self._normalize_unicode(word) for word in self.text.split(' ')])
        clean = HANDLE.sub('', text)  # Remove Twitter handles
        clean = re.sub(r'\s+', ' ', clean)  # Remove extra spaces
        clean = NEWLINE.sub(' ', clean)  # Remove newline characters

        # remove punctuation so that we can check if punctuation is all that remains
        punctless = PUNCT.sub('', clean)
        punctless = re.sub(r'\s+', '', punctless)

        # Set neat_text to the empty string if the Tweet is just a handle and/or punctuation, o.w. the cleaned text
        return '' if punctless == '' else clean.strip()

    @staticmethod
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

    @staticmethod
    def _unnormalize_unicode(word: str):
        """
        Convert Unicode Character code back to the character
        :param word:
        :return:
        """
        return word.encode().decode("unicode_escape")

    def __len__(self):
        """
        Returns the length of the Tweet's cleaned text
        :return:
        """
        return len(self._neat_text)
