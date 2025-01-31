from lib.ship import Ship
from lib.ship_placement import ShipPlacement
from lib.player import Player

class Game:

    # initialises Game with a value for rows and columns
    # creates empty list to store placed ships
    # creates dictionary of player {player_number as string: instance of Player()}
    # end_game initialised as False
    def __init__(self, rows=10, cols=10,  players = 2):
        self.rows = rows
        self.cols = cols
        self.all_ships_placed = False
        self.end_game = False
        self.players = {}
        for player_number in range(1, players + 1):
            self.players[f"Player {player_number}"] = Player(player_number)

    # checks to see if ship placement co-ordinates would place ship out of bounds
    def check_if_ship_within_board(self, orientation, length, row, col):
        if orientation == "v":
            return int(row) + int(length) > self.rows + 1 
        return int(col) + int(length) > self.cols + 1


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
        
    # removes ship from players list of unplaced ships after use
    def remove_placed_ship(self, length, player):
        for ship in player.unplaced_ships:
            if ship.length == int(length):
                player.unplaced_ships.remove(ship)
    


    # check to see if a ship is at a given co-ordinate
    def ship_at(self, row, col, player):
        for ship_placement in player.placed_ships:
            if ship_placement.covers(row, col):
                return True
        return False
    
    # check to see if ship being placed collides with already plaed ship
    def check_for_ship_collisions(self, row, col, player):
        for ship_placement in player.placed_ships:
            if (int(row), int(col)) in ship_placement.co_ordinates:
                return True
        return False
    
    # checks if all players have placed all their available ships
    def check_if_all_players_have_placed_all_ships(self):
        for player in self.players.values():
            if player.unplaced_ships == []:
                self.all_ships_placed = True
            else:
                self.all_ships_placed = False
                
    # checks given co-ordinates against co-ordinates of other placeys oplaed ships
    def check_for_missile_strike(self, missile_coordinates, player):
        for ship in self.switch_player(player).placed_ships:
                if missile_coordinates in ship.co_ordinates:
                    self.switch_player(player).placed_ships.remove(ship)
                    return "Strike!"
                else:
                    return "No strike"
    
    # switches player from given player
    def switch_player(self, current_player):
        if current_player.player_number == 1:
            player = self.players["Player 2"]
        else:
            player = self.players["Player 1"]
        return player
        
    # checks to see if all players placed ships have been sunk
    def check_if_game_ended(self):
        for player in self.players.values():
                if player.placed_ships == []:
                    self.end_game = True
                else:
                    self.end_game = False

    # returns winning message woth name of player who still have ships remaining on board
    def announce_winner(self):
        for player in self.players.values():
            if player.placed_ships != []:
                player.win = True
                return f"{player.name} has won!"
                
                
        


