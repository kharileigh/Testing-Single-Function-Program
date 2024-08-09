def diary(notes, tasks):

    notes = []
    tasks = ""
    
     # NO INPUT / 1 ARGUMENT
    if notes == [] or tasks == "":
        raise Exception("Please enter text and word to search for")
    
    # TWO ARGUMENTS
    else:
        
        # FOR LOOP -- to check every string in the list of notes
        for note in notes:

            # IF - to check if word is in current string
            if tasks in note:
                return note
            return f"{tasks} is not in notes"