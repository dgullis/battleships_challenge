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

    Returns: (str: minutes to read)
        time in minutes it'll take to read text (e.g. "200 minutes")
    """
    pass
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given an empty string
It returns 0 mins
"""
estimate_read_time("") => "0 minutes"

"""
Given a 200 words string
It returns 1 mins
"""
estimate_read_time("""Python is a powerful and versatile programming language. It is known for its readability and ease of use. Python is widely used in various domains, including web development, data science, artificial intelligence, and more. Programmers appreciate Python's simplicity and the extensive standard library that comes with it.

In Python, you can easily manipulate strings, work with data structures like lists and dictionaries, and create efficient algorithms. The community around Python is vibrant, and there are numerous libraries and frameworks available to simplify different tasks.

Whether you are a beginner or an experienced developer, Python provides a welcoming environment. Its syntax is clear and concise, making it accessible for those new to programming.

One of Python's strengths is its support for object-oriented programming, allowing developers to create modular and reusable code. Additionally, Python's dynamic typing system enables flexible and expressive coding.

Overall, Python has become a go-to language for many developers, and its influence continues to grow as it remains at the forefront of technological advancements.
Feel free to use this string for testing or any other purpose!""") => "1 minutes"

"""
Given two lowercase words
It returns an empty list
"""
extract_uppercase("hello world") => []

"""
Given a lower and a mixed case word
It returns an empty list
"""
extract_uppercase("hello WoRLD") => []

"""
Given a lowercase word and an uppercase word with an exclamation mark
It returns a list with the uppercase word, no exclamation mark
"""
extract_uppercase("hello WORLD!") => ["WORLD"]

"""
Given an empty string
It returns an empty list
"""
extract_uppercase("") => []

"""
Given a None value
It throws an error
"""
extract_uppercase(None) throws an error
```

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


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
