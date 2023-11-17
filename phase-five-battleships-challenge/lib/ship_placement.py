class ShipPlacement:
    
    # initialises with length, orietation, row and col values
    def __init__(self, length, orientation, row, col):
        self.length = length
        self.orientation = orientation
        self.row = row
        self.col = col

    # receives a value for row and col
    # checks initialised orientation value
    # if vertical:
        # if value for col does not equal the value for self.col the instance was initialised with
            # returns false
        # if col and self.col are equal:
            # check to see if row value falls between self.row and self.row_self.length
    # if horizontal:
        #same as above but replace row for col
    def covers(self, row, col):
        if self.orientation == "vertical":
            if self.col != col:
                return False
            return self.row <= row < self.row + self.length
        else:
            if self.row != row:
                return False
            return self.col <= col < self.col + self.length

    def __repr__(self):
        return f"ShipPlacement(length={self.length}, orientation={self.orientation}, row={self.row}, col={self.col})"
