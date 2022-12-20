# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods


from string import ascii_uppercase
import random

class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = random.choices(ascii_uppercase, k=9)

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        return all(letter in self.grid for letter in word)
