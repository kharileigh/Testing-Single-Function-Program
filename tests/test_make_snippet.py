from lib.make_snippet import *


"""
---- given empty string
---- returns empty string
"""
def test_given_empty_string_returns_empty_string():
    result = make_snippet("")
    assert result == ""



"""
---- given four words
---- returns string
"""
def test_given_four_words_return_string():
    result = make_snippet("I love you not")
    assert result == "I love you not"


"""
---- given five words
---- returns same string
"""
def test_given_five_words_return_string():
    result = make_snippet("I love you more today")
    assert result == "I love you more today"



"""
---- given six words
---- returns string + "..."
"""
def test_given_more_than_five_words():
    result = make_snippet("I loved you more than I did yesterday")
    assert result == "I loved you more than..."