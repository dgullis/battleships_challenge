class ShipPlacement:
    
    # initialises with given length, orietation, row and column values
    # empty list created to store the co-ordintes the ship will cover on the board
    def __init__(self, length, orientation, row, col):
        self.length = length
        self.orientation = orientation
        self.row = row
        self.col = col
        self.co_ordinates = []


    # checks to see if ship covers given row, column co-ordinates
    # adds covering co-ordinates to list as tuples (row, col)
    def covers(self, row, col):
        if self.orientation == "vertical":
            if self.col != col:
                return False
            if self.row <= row < self.row + self.length:
                self.co_ordinates.append((row, col))
                return True
        else:
            if self.row != row:
                return False
            if self.col <= col < self.col + self.length:
                self.co_ordinates.append((row, col))
                return True

    def __repr__(self):
        return f"ShipPlacement(length={self.length}, orientation={self.orientation}, row={self.row}, col={self.col})"
