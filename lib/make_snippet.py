def make_snippet(text):

    # split string into individual items in a list -- TO COUNT NUMBER OF ITEMS -- WORDS SEPARATED BY SPACES 
    words = text.split(" ")

    # if condition -- MORE THAN 5 WORDS -- DIFFERENT RETURN
    if len(words) > 5:

        # first 5 items
        first_five = words[:5]

        # join 5 items -- make singular string
        snippet = " ".join(first_five)

        # return string of 5 words + "..."
        return snippet + "..."
    
    # else condition - LESS THAN 5 WORDS / EMPTY -- RETURN GIVEN STRING
    else:
        return text