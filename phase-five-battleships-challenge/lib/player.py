from lib.ship_placement import ShipPlacement
from lib.ship import Ship

class Player():

    def __init__(self, player_number):
        self.unplaced_ships = [
            Ship(2),
            Ship(3),
            Ship(3),
            #Ship(4),
            #Ship(5),
            ]
        self.placed_ships = []
        self.win = False
        self.player_number = player_number



        