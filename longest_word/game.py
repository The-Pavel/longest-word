# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods


from string import ascii_uppercase
import random
import requests

class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = random.choices(ascii_uppercase, k=9)

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        is_in_grid =  all(letter in self.grid for letter in word)
        is_real_word = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}").json()['found']

        return is_in_grid and is_real_word
