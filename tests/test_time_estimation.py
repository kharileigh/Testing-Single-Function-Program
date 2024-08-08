import pytest
from lib.time_estimation import *


#>>>>>> GIVEN EMPTY STRING -- 0 -- RAISE EXCEPTION
def test_for_empty_text():
    with pytest.raises(Exception) as err:
        reading_estimation("")
    error_message = str(err.value)
    assert error_message == "No text entered, no estimation required"

#>>>>>> GIVEN 100 WORDS -- under 1min
def test_for_under_one_min():
    one_hundred_words = (
        """"
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        """ 
    )
    result = reading_estimation(one_hundred_words)
    assert result == "The reading estimation is: 0.5 minutes"

#>>>>>> GIVEN 200 WORDS -- 1min
def test_for_one_minute():
    two_hundred_words = (
        """"
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        """ 
    )
    result = reading_estimation(two_hundred_words)
    assert result == "The reading estimation is: 1 minutes"

#>>>>>> GIVEN 400 words -- 2mins
def test_for_two_minutes():
    four_hundreds_words = (
        """"
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        one two three four five one two three four five
        """ 
    )
    result = reading_estimation(four_hundreds_words)
    assert result == "The reading estimation is: 2 minutes"
