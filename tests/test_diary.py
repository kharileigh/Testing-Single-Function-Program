# FOR EXCEPTIONS RAISED
import pytest

from lib.diary import *


#---------------- NO ARGUMENTS GIVEN
def test_no_data_given():
    with pytest.raises(Exception) as err:
        diary([], "")
    error_message = str(err.value)
    assert error_message == "Please enter text and word to search for"


#---------------- ONE ARGUMENT, NEEDS TOO
def test_one_argument_given_text():
    with pytest.raises(Exception) as err:
        diary([], "#TODO")
    error_message = str(err.value)
    assert error_message == "Please enter text and word to search for"

def test_one_argument_given_notes():
    with pytest.raises(Exception) as err:
        diary(["#TODO", "Python Foundations", "Golden Square"], "")
    error_message = str(err.value)
    assert error_message == "Please enter text and word to search for"


#----------------- TWO ARGUMENTS
def two_arguments_given():
    notes_list = ["#TODO - 9 Aug", "Python Foundations", "Golden Square"]
    tasks = "#TODO"
    result = diary(notes_list, tasks)

    assert result == "#TODO - 9 Aug"