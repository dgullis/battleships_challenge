import time
def estimate_read_time(string):
    wpm = 200
    words = string.split()

    wps = 200/60
    readTime = time.strftime("%H:%M:%S", time.gmtime(len(words)/wps))

    print(readTime)
    return str(readTime)