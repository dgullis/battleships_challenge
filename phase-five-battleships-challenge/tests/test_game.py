from lib.game import Game
from unittest.mock import Mock, MagicMock

"""
Initialises with a length and width of 10
"""
def test_initialises_with_a_length_and_width_of_10():
    game = Game()
    assert game.rows == 10
    assert game.cols == 10

"""
Initialises with five ships of length 2, 3, 3, 4, 5
"""
def test_initialises_with_five_ships_of_right_length():
    game = Game()
    unplaced_ships = game.unplaced_ships()
    assert len(unplaced_ships) == 5
    assert unplaced_ships[0].length == 2
    assert unplaced_ships[1].length == 3
    assert unplaced_ships[2].length == 3
    assert unplaced_ships[3].length == 4
    assert unplaced_ships[4].length == 5

"""
Initialises with a totally empty board
"""
def test_initialises_with_a_totally_empty_board():
    game = Game()
    player = Mock()
    player.ships_placed = []
    for row in range(1, 11):
        for col in range(1, 11):
            assert not game.ship_at(row, col, player)

"""
When we place a ship
Then its place on the board is marked out
"""
def test_when_we_place_a_ship_then_its_place_on_the_board_is_marked_out():
    game = Game()
    player = Mock()
    game.place_ship(player, 2, "vectical", 3, 2)
    ship_placement = MagicMock()
    ship_placement.length = 2
    ship_placement.orientation="vertical"
    ship_placement.row=3
    ship_placement.col=2
    ship_placement.covers.side_effect = [True, True, False, False, False, False]
    player.ships_placed = [ship_placement]
    assert game.ship_at(3, 2, player)
    assert game.ship_at(4, 2, player)
    assert not game.ship_at(3, 3, player)
    assert not game.ship_at(4, 3, player)
    assert not game.ship_at(3, 1, player)
    assert not game.ship_at(4, 1, player)
