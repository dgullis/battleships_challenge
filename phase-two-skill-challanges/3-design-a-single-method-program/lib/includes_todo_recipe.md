# Includes #TODO Function Design Recipe

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python

def includes_todo(text):
    """Checks if text contains #TODO

    Parameters:
        text: a string containing words (e.g. "hello WORLD")

    Returns:
        todo: a boolean based on whether text contained #TODO
    """
    pass
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

"""
Given a string not containing #TODO
It returns a False
"""
includes_todo("hello world") => False

"""
Given a string containing #TODO
It returns a True
"""
includes_todo("#TODO Brush Teeth") => True

"""
Given an empty string
It returns a False
"""
includes_todo("") => False

"""
Given a string containing lowercase #TODO
It returns a True
"""
includes_todo("#todo Tidy Up") => True

"""
Given a string containing #TODO at the end
It returns a True
"""
includes_todo("Tidy up #TODO") => True

"""
Given a string containing #TODO in the middle
It returns a True
"""
includes_todo("Tidy #TODO Up") => True

"""
Given a non string value 
It throws an error
"""
includes_todo(5) throws an error
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]

```

---
