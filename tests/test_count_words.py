#A function called count_words that takes a string as an argument and returns the number of words in that string
from lib.count_words import *


#>>>> GIVEN EMPTY STRING, RETURN 0
def test_count_words_empty_string():
    result = count_words("")
    assert result == 0


#>>>> GIVEN STRING WITH 10 CHARACTERS, RETURN 10
def test_count_words_ten_characters():
    result = count_words("0123456789")
    assert result == 10