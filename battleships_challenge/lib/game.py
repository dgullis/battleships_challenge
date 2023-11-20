from lib.ship import Ship
from lib.ship_placement import ShipPlacement
from lib.player import Player

class Game:

    # initialises every instance of Game with a value for rows and columns
    # creates empty list to store placed ships
    def __init__(self, rows=10, cols=10,  players = 2):
        self.rows = rows
        self.cols = cols

        self.all_ships_placed = False
        self.end_game = False
        
        self.players = {}
        for player_number in range(1, players + 1):
            self.players[f"Player {player_number}"] = Player(player_number)

    # calls the ship class 5 times
    # parameter passed into each call represents length of ship
    # def unplaced_ships(self):
    #     return [
    #         Ship(2),
    #         Ship(3),
    #         #Ship(3),
    #         #Ship(4),
    #         #Ship(5),
    #     ]

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
        player.placed_ships.append(ship_placement)
        
    # removes ship from players list of ships after use
    def remove_placed_ship(self, length, player):
        for ship in player.unplaced_ships:
            if ship.length == int(length):
                player.unplaced_ships.remove(ship)
    


    # iterates over players list of placed ships
    # 
    def ship_at(self, row, col, player):
        for ship_placement in player.placed_ships:
            if ship_placement.covers(row, col):
                return True
        return False
    
    def check_for_ship_collisions(self, row, col, player):
        for ship_placement in player.placed_ships:
            if (int(row), int(col)) in ship_placement.co_ordinates:
                return True
        return False
    
    def check_for_missile_strike(self, row, col, player):
        pass
    
    def check_turn(self, player_1_turn):
        if player_1_turn == True:
            player = self.players["Player 1"]
        else:
            player = self.players["Player 2"]
        return player

    def check_if_game_ended(self):
        for player in self.players.values():
                if player.placed_ships == []:
                    self.end_game = True
                else:
                    self.end_game = False

    def announce_winner(self):
        for player in self.players.values():
            if player.placed_ships != []:
                player.win = True
                return f"{player.name} has won!" + "\n"
                
                
        


