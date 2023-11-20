from lib.player import Player

class UserInterface:
    def __init__(self, io, game, players = 2):
        self.io = io
        self.game = game

    # game starts with welcome messages
    # player names are set
    # player is set to player 1
    def run(self):
        self._show("Welcome to the game!")
        self._prompt_for_player_names()
        self._show("Set up your ships first.")

        player = next(filter(lambda p: p.player_number == 1, self.game.players.values()), None)

        # players prompted to plae ships until both players have placed all ships
        while not self.game.all_ships_placed:
            
            self._show(f"It is {player.name}'s turn")
            self._show("You have these ships remaining: {}".format(
                self._ships_unplaced_message("string", player)))
            self._prompt_for_ship_placement(player)
            self._show("This is your board now:")
            self._show(self._format_board(player))
        
            player = self.game.switch_player(player)
        
            self.game.check_if_all_players_have_placed_all_ships()
        
        # players prompted to select co-ordinates for their missiles
        # when a player has sunk all of the other players ships, they're declared winner        
        while not self.game.end_game:
            self.game.check_if_game_ended()

            self._show(f"It is {player.name}'s turn")

            missile_coordinates = self._prompt_for_missile_coordinates()

            missile_strike_message = self.game.check_for_missile_strike(missile_coordinates, player)
            
            self._show(missile_strike_message)
            
            self.game.check_if_game_ended()
    
            player = self.game.switch_player(player)
            
        self._show(self.game.announce_winner())

    # Display/output a message to the CLI
    def _show(self, message):
        self.io.write(message + "\n")

    # Display/output a message and prompt user for input, return that input
    def _prompt(self, message):
        self.io.write(message + "\n")
        return self.io.readline().strip()

    # Display/output a mesage showing the remaining(yet to be placed) ships
    def _ships_unplaced_message(self, format, player):
        ship_lengths = [str(ship.length) for ship in player.unplaced_ships]
        if format == "string":
            return ", ".join(ship_lengths)
        return ship_lengths

    # prompts user for input and compares input against list of valid option
    def _prompt_and_validate(self, prompt_msg, validation_options):
            user_input = self._prompt(prompt_msg)
            while user_input not in validation_options:
                self._show("Invalid input, choose again...")
                user_input = self._prompt(prompt_msg)
            return user_input

    # gets values for ship length, orientation, row and column from user
    # will only continue when each input is valid
    def _prompt_for_ship_placement(self, player):
        ship_length = self._prompt_and_validate("Which do you wish to place?", self._ships_unplaced_message("list", player))
        ship_orientation = self._prompt_and_validate("Vertical or horizontal? [vh]", ["v", "h"])
        ship_row = self._prompt_and_validate("Which row?", [str(num) for num in range(1,11)])
        ship_col = self._prompt_and_validate("Which column?", [str(num) for num in range(1,11)])

        while self.game.check_if_ship_within_board(ship_orientation, ship_length, ship_row, ship_col):
                self._show("out of bounds, choose again...")
                ship_row = self._prompt("Which row?")
                ship_col = self._prompt("Which column?")

        while self.game.check_for_ship_collisions(ship_row, ship_col, player):
            self._show("ship collision, choose again...")
            ship_row = self._prompt("Which row?")
            ship_col = self._prompt("Which column?")

        # when all placements are valid
        # ship is placed
        self._show("OK.")
        self.game.place_ship(player,
            length=int(ship_length),
            orientation={"v": "vertical", "h": "horizontal"}[ship_orientation],
            row=int(ship_row),
            col=int(ship_col),
            )
        self.game.remove_placed_ship(ship_length, player)
    
    # gets missile co-ordinates from user
    # returns these as a tuple of integers (row, column)
    def _prompt_for_missile_coordinates(self):
        raw_missile_coordinates = self._prompt("Choose missile co-ordinates [row, column]")
        missile_coordinates = raw_missile_coordinates.split(",")
        missile_row = missile_coordinates[0].strip()
        missile_column = missile_coordinates[1].strip()
        return (int(missile_row), int(missile_column))
    
    def _prompt_for_player_names(self):
        for player in self.game.players.values():
            player.name = self._prompt(f"Player {player.player_number} enter your name")
    
   # outputs board to terminal
   # ship locations represented by "S", empty grid spaces represented by "."
    def _format_board(self, player):
        rows = []
        for row in range(1, self.game.rows + 1):
            row_cells = []
            for col in range(1, self.game.cols + 1):
                if self.game.ship_at(row, col, player):
                    row_cells.append("S")
                else:
                    row_cells.append(".")
            rows.append("".join(row_cells))
        return "\n".join(rows)
        