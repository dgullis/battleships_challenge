# Battleships Class System Design

## Introduction
How do we figure out how to break our program up
into classes? There are two common approaches to this:

1. **Emergent Design**  
   Start with a single class, and then extract out new classes when it seems
   like it is doing too much.

2. **Planned Design**  
   Design a multi-class system and then build it, updating your design as you
   learn where you were wrong at first.

You can also use a mix of both.

Here's our Multi-Class Planned Design Recipe

# Multi-Class Planned Design Recipe
 
## 1. Describe the Problem

Place ship on board
multiple ship sizes
ships constrained to board
ships cannot overlap
can fire at opponent's board
2 player game

Command Line Interface Input:
enter ship positions
enter shots
choose direction of ship 

Output:
when opponent's ship has sunk
when game ends - win or loss


```
### 1
As a player
So that I can prepare for the game
I would like to place a ship in a board location

### 2
As a player
So that I can play a more interesting game
I would like to have a range of ship sizes to choose from

### 3
As a player
So the game is more fun to play
I would like a nice command line interface that lets me enter ship positions and
shots using commands.

### 4
As a player
So that I can create a layout of ships to outwit my opponent
I would like to be able to choose the directions my ships face in

### 5
As a player
So that I can have a coherent game
I would like ships to be constrained to be on the board

### 6
As a player
So that I can have a coherent game
I would like ships to be constrained not to overlap

### 7
As a player
So that I can win the game
I would like to be able to fire at my opponent's board

### 8
As a player
So that I can refine my strategy
I would like to know when I have sunk an opponent's ship

### 9
As a player
So that I know when to finish playing
I would like to know when I have won or lost

### 10
As a player
So that I can consider my next shot
I would like to be able to see my hits and misses so far

### 11
As a player
So that I can play against a human opponent
I would like to play a two-player game
```

## 2. Design the Class System

Design the interfaces of each of your classes and how they will work together
to achieve the job of the program. You can use diagrams to visualise the
relationships between classes.

Consider pulling out the key verbs and nouns in the problem description to
help you figure out which classes and methods to have.

Steps 3, 4, and 5 then operate as a cycle.

### Files and Classes
- ship.py  
Ship

- ship_placement.py  
ShipPlacement  
    __init__- length, orientation, row, col
    covers - row, col
    __repr__

- user_interface.py  
UserInterface  
    __init__ - io, game
    run -
    _show - message
    _prompt - message
    _ships_unplaced_message - 
    _prompt_for_ship_placement - 
    _format_board - 

- game.py  
Game  
    __int__ - rows=10, columns=10
    unplaced_ships
    place_ships - length, orientation, row, col
    ship_at - row, col


### Functionality Needed:
- [x] Place ship on board
- [x] multiple ship sizes
- [x] ships constrained to board
- [ ] ships cannot overlap
- [ ] 2 player game
- [ ] can fire at opponent's board


Command Line Interface Input:
- [x] enter ship positions
- [x] choose direction of ship
- [ ] enter shots

Output:
- [ ] when opponent's ship has sunk
- [ ] when game ends - win or loss

## 3. Create Examples as Integration Tests

Create examples of the classes being used together in different situations
and combinations that reflect the ways in which the system will be used.

Encode one of these as a test and move to step 4.

- test_game.py

"""
Initialises with a length and width of 10
"""

def test_initialises_with_a_length_and_width_of_10(); 

"""
Initialises with five ships of length 2, 3, 3, 4, 5
"""
def test_initialises_with_five_ships_of_right_length():

"""
Initialises with a totally empty board
"""
def test_initialises_with_a_totally_empty_board():
    
"""
When we place a ship
Then its place on the board is marked out
"""
def test_when_we_place_a_ship_then_its_place_on_the_board_is_marked_out():

    

- test_ship_placement.py

"""
Initialises with a length, orientation, row, and col
"""
def test_initialises_with_a_length_orientation_row_and_col():

"""
Checks if vertical ships cover a given row and col
"""
def test_checks_if_vertical_ships_cover_a_given_row_and_col():

"""
Checks if horizontal ships cover a given row and col
"""
def test_checks_if_horizontal_ships_cover_a_given_row_and_col():

"""
Has a friendly string representation
"""
def test_has_a_friendly_string_representation():


- test_ship.py
"""
Initialises with a given length
"""
def test_initialises_with_a_given_length():

- test_user_interface_integration.py

class TestUserInterface(unittest.TestCase):
    def test_ship_setup_scenario(self):


## 4. Create Examples as Unit Tests

Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail.

Encode one of these as a test and move to step 5.

## 5. Implement the Behaviour

For each example you create as a test, implement the behaviour that allows the
class to behave according to your example.

Then return to step 3 until you have addressed the problem you were given. You
may also need to revise your design, for example if you realise you made a
mistake earlier.


* Remember that user stories don't map to classes 1:1. You'll need to digest the
  full problem and then develop a multi-class system that meets the user's
  needs.
* Don't worry about user interface or input-output. That means you shouldn't be
  using `input()` and only use `print()` for debugging purposes.

---