"""
What we need to implement:
    - Error Checking and Throwing -
        - vh - input for Vertical/Horizontal should only accept hv (any case)
        - Board Rows and Cols - Restricted to 1-10
        - Ship Size
        - Re-prompt  if one of these threw an error
    
    - Loop for Game - allowing multiple ships to be placed
        - Remove ship when used
        - Ships Cannot Overlap
    - Player Class for multiple players
    - Output Winner function in Game class
    - Shooting and Sinking Ships Functionality
"""



"""
Function => test valid move (inputed row, inputed column, board rows, boards cols)

Input = invalid

While input == invalid:

Ask the prompt questions

If given row or given column are > 10
    input is invalid
For vertical ships
If given row + ship length > 10
    input is invalid
For horizontal ships
If given col + ship length > 10
    input is invalid

When answers to prompt questions are all valid
Input = valid
Create board

Note - this would work for boards 10 x 10 but we would need to receive board size and use this value 
"""



def _prompt_for_ship_placement(self):
        ship_length = self._prompt("Which do you wish to place?")
        ship_orientation = self._prompt("Vertical or horizontal? [vh]")
        ship_row = self._prompt("Which row?")
        ship_col = self._prompt("Which column?")

        ### check if its a valid placement, if so output OK! and place ship
        ### create out of bounds function

        
        ### We can put a call for this function in either the place_ship function or call it before placing the ship
        ### if the ship would be out of bounds (we can check this by seeing if the value of a ship segment would be in a negative
        ### row or coulumn or greater than the size of the board (which is stored in game.rows and game.cols))

        if True:
            self._show("OK.")
            self.game.place_ship(
                length=int(ship_length),
                orientation={"v": "vertical", "h": "horizontal"}[ship_orientation],
                row=int(ship_row),
                col=int(ship_col),
            )
        ### else, output INVALID! and ask for new values
        else:
            self._show("INVALID!")
            ship_length = self._prompt("Which do you wish to place?")
            ship_orientation = self._prompt("Vertical or horizontal? [vh]")
            ship_row = self._prompt("Which row?")
            ship_col = self._prompt("Which column?")
            
            self._show("OK.")
            self.game.place_ship(
                length=int(ship_length),
                orientation={"v": "vertical", "h": "horizontal"}[ship_orientation],
                row=int(ship_row),
                col=int(ship_col),
            )
