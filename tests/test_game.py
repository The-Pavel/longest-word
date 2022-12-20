# tests/test_game.py
from longest_word.game import Game
class TestGame:
    def test_game_initialization(self):
        # setup
        game = Game()
        # exercise
        # verify
        assert len(game.grid) == 9
        assert all(letter.isalpha() for letter in game.grid)
        # teardown

    def test_word_validity(self):
        # setup
        game = Game()
        game.grid = ["T", "O", "M", "A", "T", "O"]
        word = "TOMATO"
        # exercise
        # verify
        assert game.is_valid(word)
        # teardown

    def test_word_invalidity(self):
        # setup
        game = Game()
        game.grid = ["T", "O", "M", "A", "T", "O"]
        word = "POTATO"
        # exercise
        # verify
        assert game.is_valid(word) is False
        assert game.grid == ["T", "O", "M", "A", "T", "O"]
        # teardown
