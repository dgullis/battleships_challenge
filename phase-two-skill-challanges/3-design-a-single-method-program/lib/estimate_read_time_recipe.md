# Estimate Read Time Function Design Recipe


## 1. Describe the Problem

_As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute._

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python

def estimate_read_time(text):
    """Estimates how long it takes to read the given text

    Parameters: (str: text)
        text: a string containing words (e.g. "hello WORLD")

    Returns: (str: time to read)
        time in minutes it'll take to read text (e.g. "200 minutes")
    """
    pass
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

"""
Given an empty string
It returns 0 mins
"""
estimate_read_time("") => "0 minutes"

"""
Given a 200 words string
It returns 1 mins
"""
estimate_read_time("word"*200) => "1 minutes"


_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]

```

Ensure all test function names are unique, otherwise pytest will ignore them!

---

