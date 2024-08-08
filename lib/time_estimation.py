def reading_estimation(text):
    
    # split text -- individual words
    words = text.split()

    # count number of words
    word_count = len(words)

    # global scope - return value
    estimation = 0


    # 0 words -- ERROR
    if word_count == 0:
        raise Exception("No text entered, no estimation required")

    # LESS THAN 200 -- round to 1 decimal place
    if word_count < 200:
        estimation = round(word_count/200, 1)

    # 200 OR MORE -- round to integer
    if word_count > 200:
        estimation = round(word_count/200)
        
    # 200 words
    if word_count == 200:
        estimation = word_count/200

    # return estimation
    total_time = f"The reading estimation is: {estimation} minutes"
    return total_time