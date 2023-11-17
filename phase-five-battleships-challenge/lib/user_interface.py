class UserInterface:
    # 
    def __init__(self, io, game):
        self.io = io
        self.game = game

    # Starts the game - outputting a welcome message using the private show method
    # Displays unplaced ships using private _ships_unplaced_message() method
    # Prompts user for input using private _promp_for_ship_placement() method
    # Output the board using the private _format_board() method
    def run(self):
        self._show("Welcome to the game!")
        self._show("Set up your ships first.")
        self._show("You have these ships remaining: {}".format(
            self._ships_unplaced_message("string")))
        self._prompt_for_ship_placement()
        self._show("This is your board now:")
        self._show(self._format_board())

    # Display/output a message to the CLI
    def _show(self, message):
        self.io.write(message + "\n")

    # Display/output a message and prompt user for input, return that input
    def _prompt(self, message):
        self.io.write(message + "\n")
        return self.io.readline().strip()

    # Display/output a mesage showing the remaining(yet to be placed) ships
    def _ships_unplaced_message(self, format):
        ship_lengths = [str(ship.length) for ship in self.game.unplaced_ships()]
        if format == "string":
            return ", ".join(ship_lengths)
        return ship_lengths

    def validity(self, input_value, valid_list):
        if input_value in valid_list:
            return True
        return False

    # Prompt user for input - ship length, orientation, row and col co-ordinates, using _prompt method
    # Store the returned values in their respective variables
    # Place the ship using the above variables as parameters for the place_ship() function in the Game class
    # if any inputs invalid error message shown and re-prompt until valid input
    def _prompt_for_ship_placement(self):
        ship_length = self._prompt("Which do you wish to place?")
        while not self.validity(ship_length, self._ships_unplaced_message("list")):
            self._show("invalid ship, choose again...")
            ship_length = self._prompt("Which do you wish to place?")

        ship_orientation = self._prompt("Vertical or horizontal? [vh]")
        while not self.validity(ship_orientation, ["v", "h"]):
            self._show("invalid orientation, choose again...")
            ship_orientation = self._prompt("Vertical or horizontal? [vh]")

        ship_row = self._prompt("Which row?")
        while not self.validity(int(ship_row), [num for num in range(1,11)]):
            self._show("out of bounds, choose again...")
            ship_orientation = self._prompt("Which row?")

        ship_col = self._prompt("Which column?")
        while not self.validity(int(ship_col), [num for num in range(1,11)]):
            self._show("out of bounds, choose again...")
            ship_orientation = self._prompt("Which column?")

        # while ship_length not in [str(ship.length) for ship in self.game.unplaced_ships()]:
        #     self._show("invalid ship, choose again...")
        #     ship_length = self._prompt("Which do you wish to place?")
        
        # ship_orientation = self._prompt("Vertical or horizontal? [vh]")
        # while ship_orientation not in ["v", "h"]:
        #     self._show("invalid orientation, choose again...")
        #     ship_orientation = self._prompt("Vertical or horizontal? [vh]")
        
        # ship_row = self._prompt("Which row?")
        # while ship_row < 1 or ship_row > self.game.rows:
        #     self._show("out of bounds, choose again...")
        #     self._prompt("Which row?")
        
        # ship_col = self._prompt("Which column?")
        # while ship_col < 1 or ship_row > self.game.cols:
        #     self._show("out of bounds, choose again...")
        #     self._prompt("Which column?")

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

        ### check if its a valid placement, if so output OK! and place ship
        # valid_placement = self.is_valid(self.game, 
        #         length=int(ship_length),
        #         orientation={"v": "vertical", "h": "horizontal"}[ship_orientation],
        #         row=int(ship_row),
        #         col=int(ship_col))

        # if valid_placement:
        self._show("OK.")
        self.game.place_ship(
            length=int(ship_length),
            orientation={"v": "vertical", "h": "horizontal"}[ship_orientation],
            row=int(ship_row),
            col=int(ship_col),
        )
        ### else, output INVALID! and ask for new values
        # else:
        #     self._show("INVALID!")
        #     self._show("You have these ships remaining: {}".format(
        #         self._ships_unplaced_message()))
        #     ship_length = self._prompt("Which do you wish to place?")
        #     ship_orientation = self._prompt("Vertical or horizontal? [vh]")
        #     ship_row = self._prompt("Which row?")
        #     ship_col = self._prompt("Which column?")
            
        #     self._show("OK.")
        #     self.game.place_ship(
        #         length=int(ship_length),
        #         orientation={"v": "vertical", "h": "horizontal"}[ship_orientation],
        #         row=int(ship_row),
        #         col=int(ship_col),
        #     )
    

    # Output the current layout of the board
    # Generate the board row by row in the for loop
    # Give ship_at function from Game class co-ordinates of a cell, if it returns True,
    # set cell to S, else set to .
    # append cell to row_cells list
    # append joined row_cells list to rows list
    def _format_board(self):
        rows = []
        for row in range(1, self.game.rows + 1):
            row_cells = []
            for col in range(1, self.game.cols + 1):
                if self.game.ship_at(row, col):
                    row_cells.append("S")
                else:
                    row_cells.append(".")
            rows.append("".join(row_cells))
        return "\n".join(rows)


    # def is_valid(self, game, length, orientation, row, col):
    #     if (row > 0 and row < game.rows) and (col > 0 and col < game.cols):
    #         if orientation == "vertical" and (row + length) <= game.rows:
    #             return True
    #         elif orientation == "horizontal" and (col + length) <= game.cols:
    #             return True
    #     return False
