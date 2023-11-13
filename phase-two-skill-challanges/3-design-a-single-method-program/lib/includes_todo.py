def includes_todo(text):
    if type(text) != str:
        raise Exception("Function only accepts strings!")

    words = text.upper().split()

    for word in words:
        if word == "#TODO":
            return True
    return False
