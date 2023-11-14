# To Do List Class Design Recipe


## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class ToDoList:
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Side effects:
        #   Sets the tasks variable of the object to an empty list
        pass # No code here yet

    def add(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object
        pass # No code here yet

    def format(self):
        # Returns:
        #   Strings showing the remaining tasks 
        pass # No code here yet

    def complete(self, task):
        # Returns:
        #   Nothing
        # Side-effects:
        #   removes task from the tasks variable
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Add a task
Adds task to  tasks attribute of object and formats it for output
"""
todos = ToDoList()
todos.add("Walk the dog")
todos.format() # => "Walk the dog"

"""
Given a name and no task
#remind raises an exception
"""
todos = ToDoList()
todos.add("Walk the dog")
todos.add("Wash the dog")
todos.add("Walk the cat")
todos.format() # => 
"""Walk the dog"
"Wash the dog"
"Walk the cat"""

"""
Mark a a task as complete
#remind still reminds the user to do the task, even though it looks odd
"""
todos = ToDoList()
todos.add("Walk the dog")
todos.add("Wash the dog")
todos.add("Walk the cat")
todos.complete("Wash the dog")
todos.format() # => 
"""Walk the dog"
"Walk the cat"""
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

---
