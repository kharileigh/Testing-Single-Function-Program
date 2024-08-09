def diary(notes, tasks):

    
     # NO INPUT / 1 ARGUMENT
    if notes == [] and tasks == "":
        raise Exception("Please enter text and word to search for")
    elif notes == [] and tasks != "":
        raise Exception("Please enter your notes")
    elif notes != [] and tasks == "":
        raise Exception("Please enter text to search for")
    
    # TWO ARGUMENTS
    # FOR LOOP -- to check every string in the list of notes
    for note in notes:
        print(note)
        # YES - word in string, retun string
        if tasks in note:
            return note
        
    # NO - return message not found    
    return f"{tasks} is not in notes"