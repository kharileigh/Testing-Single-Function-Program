from lib.make_snippet import *


#>>>> GIVEN EMPTY STRING, RETURNS EMPTY STRING
def test_given_empty_string_returns_empty_string():
    result = make_snippet("")
    assert result == ""



#>>>>> GIVEN LESS THAN 5 WORDS, RETURNS STRING
def test_given_four_words_return_string():
    result = make_snippet("I love you not")
    assert result == "I love you not"


#>>>>> GIVEN 5 WORDS, RETURNS STRING
def test_given_five_words_return_string():
    result = make_snippet("I love you more today")
    assert result == "I love you more today"



#>>>>> GIVEN MORE THAN 5 WORDS, RETURNS ONLY 5 WORDS & ...
def test_given_more_than_five_words():
    result = make_snippet("I loved you more than I did yesterday")
    assert result == "I loved you more than..."