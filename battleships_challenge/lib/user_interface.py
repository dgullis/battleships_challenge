from lib.player import Player

class UserInterface:
    # 
    def __init__(self, io, game, players = 2):
        self.io = io
        self.game = game
        self.players = {}
        # for player_number in range(1, players + 1):
        #     self.players[f"Player {player_number}"] = Player(player_number)


    # Starts the game - outputting a welcome message using the private show method
    # Displays unplaced ships using private _ships_unplaced_message() method
    # Prompts user for input using private _promp_for_ship_placement() method
    # Output the board using the private _format_board() method
    def run(self):
        self._show("Welcome to the game!")
        self._show("Set up your ships first.")

        self._prompt_for_player_names()
        
        switch = True

        while not self.game.all_ships_placed:
            
            player = self.game.switch_player(switch)

            self._show(f"It is {player.name}'s turn")
            self._show("You have these ships remaining: {}".format(
                self._ships_unplaced_message("string", player)))
            self._prompt_for_ship_placement(player)
            self._show("This is your board now:")
            self._show(self._format_board(player))
        
            switch= not switch
        
            self.game.check_if_all_players_have_placed_all_ships()
                
        while not self.game.end_game:
            self.game.check_if_game_ended()

            player = self.game.switch_player(switch)
            
            self._show(f"It is {player.name}'s turn")
        
            missile_coordinates = self._prompt_for_missile_coordinates()
            
            for ship in self.game.switch_player(player).placed_ships:
                if missile_coordinates in ship.co_ordinates:
                    self._show("Strike!")
                    self.game.switch_player(player).placed_ships.remove(ship)
                else:
                    self._show("No strike")
            
            self.game.check_if_game_ended()
            switch = not switch

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

    # def validity(self, input_value, valid_list):
    #     if input_value in valid_list:
    #         return True
    #     return False
    
    def _prompt_and_validate(self, prompt_msg, validation_options):
            user_input = self._prompt(prompt_msg)
            while user_input not in validation_options:
                self._show("Invalid input, choose again...")
                user_input = self._prompt(prompt_msg)
            return user_input

    # Prompt user for input - ship length, orientation, row and col co-ordinates, using _prompt method
    # Store the returned values in their respective variables
    # Place the ship using the above variables as parameters for the place_ship() function in the Game class
    # if any inputs invalid error message shown and re-prompt until valid input
    def _prompt_for_ship_placement(self, player):
        ship_length = self._prompt_and_validate("Which do you wish to place?", self._ships_unplaced_message("list", player))
        ship_orientation = self._prompt_and_validate("Vertical or horizontal? [vh]", ["v", "h"])
        ship_row = self._prompt_and_validate("Which row?", [str(num) for num in range(1,11)])
        ship_col = self._prompt_and_validate("Which column?", [str(num) for num in range(1,11)])

        if ship_orientation == "v":
            while int(ship_row) + int(ship_length) > self.game.rows + 1:
                self._show("out of bounds, choose again...")
                ship_row = self._prompt("Which row?")
                ship_col = self._prompt("Which column?")

        if ship_orientation == "h":
            while int(ship_col) + int(ship_length) > self.game.cols + 1:
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
    
    def _prompt_for_missile_coordinates(self):
        raw_missile_coordinates = self._prompt("Choose missile co-ordinates [row, column]")
        missile_coordinates = raw_missile_coordinates.split(",")
        missile_row = missile_coordinates[0].strip()
        missile_column = missile_coordinates[1].strip()
        #print(missile_row, missile_column)
        return (int(missile_row), int(missile_column))
    
    def _prompt_for_player_names(self):
        for player in self.game.players.values():
            player.name = self._prompt(f"Player {player.player_number} enter your name")
    



    # Output the current layout of the board
    # Generate the board row by row in the for loop
    # Give ship_at function from Game class co-ordinates of a cell, if it returns True,
    # set cell to S, else set to .
    # append cell to row_cells list
    # append joined row_cells list to rows list
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
        