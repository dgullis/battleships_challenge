# A function called make_snippet that takes a string as an argument and returns the first five words and then a '...' if there are more than that.

def make_snippet(string):
    words = string.split()
    fiveWords = words[:5]
    if len(words)  > 5:
        fiveWords.append("...")
    return (f"{' '.join(word for word in fiveWords)}")