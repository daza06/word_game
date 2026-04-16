from word_game import select_word, check_guess
import pytest


def test_select_word():
    word1 = select_word("words.csv")
    word2 = select_word("words.csv")

    assert len(word1) == 5
    assert len(word2) == 5


def test_check_guess():
    secret = "apple"

    result1 = check_guess(secret, "apple")
    result2 = check_guess(secret, "angle")

    assert result1 == ["G", "G", "G", "G", "G"]
    assert len(result2) == 5


def test_check_guess_exact():
    assert check_guess("apple", "apple") == ["G", "G", "G", "G", "G"]


def test_word_is_valid_length():
    word = select_word("words.csv")
    assert isinstance(word, str)
    assert len(word) == 5

pytest.main(["-v", "--tb=line", "-rN", __file__])