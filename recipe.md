<!--------------------------------------------------------------------------------------->
<!------------------CORRECT DESIGN RECIPE -------------------------------------------------->
## 1. Describe the Problem
As a user
So that I can find my tasks among all my notes
I want to check if a line from my notes includes the string '#TODO'

------ User wants to find a line from notes with a specific word given
------ Find a given string in a list of strings that includes word given


## 2. Design the Function Signature
-- def diary(notes, tasks):
        Parameters :
        tasks -- what user is looking for : "#TODO"
        notes -- list of notes holding all tasks

        Functionality :
        loop through every string in notes
        checking if current string includes given word (tasks)
        if includes word, return that string to user

        Returns :
        string including word : f"Tasks {word}"

## 3. Create Examples as Tests

# NO ARGUMENTS
diary() => raises error, need to input data 
	
# ONE ARGUMENT, NEEDS TWO
diary() => raises error, need to input data
		
# TWO ARGUMENTS
diary() => returns string including word 

## 4. Implement the Behaviour
FAIL TEST -- CODE -- PASS TEST -- FAIL NEW TEST -- REFACTOR -- PASS TEST










<!----------------------------------------------------------------->
<!----------------------------------------------------------------->
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
FAIL TEST -- CODE -- PASS TEST -- FAIL NEW TEST -- REFACTOR -- PASS TEST




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
FAIL TEST -- CODE -- PASS TEST -- FAIL NEW TEST -- REFACTOR -- PASS TEST



<!----------------------------------------------------------------->
<!----------------------------------------------------------------->
## 1. Describe the Problem
-- calculate reading time for text

## 2. Design the Function Signature
-- def reading_estimation(text):
				
        split text into singular words
        count length singular words
        word count divided by 200
        estimation equals f"Reading time estimation is : {word count} minutes"
        return estimation

## 3. Create Examples as Tests

    -- empty
    -- 100 words -- below 1 minute
    -- 200 words -- equals 1 minute
    -- 400 words -- 2 minutes

## 4. Implement the Behaviour
FAIL TEST -- CODE -- PASS TEST -- FAIL NEW TEST -- REFACTOR -- PASS TEST










