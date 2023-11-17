from dataclasses import dataclass

# initialises any instance of ship with a length attribute
    # e.g. Ship(5) = ship with length = 5
@dataclass
class Ship:
    length: int
