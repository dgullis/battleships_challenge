from lib.ship import Ship
from lib.ship_placement import ShipPlacement


class Game:

    # initialises every instance of Game with a value for rows and columns
    # creates empty list to store placed ships
    def __init__(self, rows=10, cols=10):
        self.rows = rows
        self.cols = cols
        self.end_game = False

    # calls the ship class 5 times
    # parameter passed into each call represents length of ship
    def unplaced_ships(self):
        return [
            Ship(2),
            Ship(3),
            Ship(3),
            Ship(4),
            Ship(5),
        ]

    # creates an instance of ShipPlacement passing in values for:
        # length, orientation, row, col
    # appends ships_placed list with created instance of ShipPlacement
    def place_ship(self, player, length, orientation, row, col):
        ship_placement = ShipPlacement(
            length=length,
            orientation=orientation,
            row=row,
            col=col,
        )
        player.ships_placed.append(ship_placement)

    # iterates over items in ships_placed list
        # for each iteration it calls ship_placement.covers() with the given
            # row and col values
        # if this returns true the function returns true, otherwise returns false
    def ship_at(self, row, col, player):
        for ship_placement in player.ships_placed:
            if ship_placement.covers(row, col):
                return True
        return False
