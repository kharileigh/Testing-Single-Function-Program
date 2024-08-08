A function called make_snippet that takes a string as an argument and returns the first five words and then '...' if there are more than that 

## 1. Describe the Problem
<!-- Put or write the user story here. Add any clarifying notes you might have. -->
from a given string, only return first 5 words


## 2. Design the Function Signature
<!-- Include the name of the function, its parameters, return value, and side effects. -->
def make_snippet(str):
    
    split string -- count words in string

    if condition -- string > 5 words
        take first 5
        join 
        return first 5 + "..."

    else:
        (empty string, 5 words or less)
        return same string


## 3. Create Examples as Tests
<!-- Make a list of examples of what the function will take and return. -->

>>>> GIVEN EMPTY STRING, RETURNS EMPTY STRING

>>>>> GIVEN LESS THAN 5 WORDS, RETURNS STRING

>>>>> GIVEN MORE THAN 5 WORDS, RETURNS ONLY 5 WORDS & ...



## 4. Implement the Behaviour
<!-- After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour -->




<!----------------------------------------------------------------->
<!----------------------------------------------------------------->
A function called count_words that takes a string as an argument and returns the number of words in that string

## 1. Describe the Problem
<!-- Put or write the user story here. Add any clarifying notes you might have. -->
from a given string, return number of words


## 2. Design the Function Signature
<!-- Include the name of the function, its parameters, return value, and side effects. -->
def count_words(text):

    count = len(text)
    return count



## 3. Create Examples as Tests
<!-- Make a list of examples of what the function will take and return. -->

>>>> GIVEN EMPTY STRING, RETURN 0

>>>> GIVEN STRING WITH 10 CHARACTERS, RETURN 10


## 4. Implement the Behaviour
<!-- After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour -->
