import unittest
import pytest
from lib.user_interface import UserInterface
from lib.game import Game
from tests.terminal_interface_helper_mock import TerminalInterfaceHelperMock
from lib.player import Player
from unittest.mock import patch


class TestUserInterface(unittest.TestCase):
    @pytest.mark.skip
    def test_ship_setup_scenario(self):
        io = TerminalInterfaceHelperMock()
        game = Game()
        player1 = Player(1)
        player2 = Player(2)
        interface = UserInterface(io, game)
        io.expect_print("Welcome to the game!")
        io.expect_print("Set up your ships first.")
        io.expect_print("It is Player 1's turn")
        io.expect_print("You have these ships remaining: 2, 3, 3, 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("2")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("3")
        io.expect_print("Which column?")
        io.provide("2")
        io.expect_print("OK.")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..........",
            "..........",
            ".S........",
            ".S........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
        ]))
        io.expect_print("It is Player 2's turn")
        io.expect_print("You have these ships remaining: 2, 3, 3, 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("5")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("3")
        io.expect_print("Which column?")
        io.provide("5")
        io.expect_print("OK.")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..........",
            "..........",
            "....S.....",
            "....S.....",
            "....S.....",
            "....S.....",
            "....S.....",
            "..........",
            "..........",
            ".........."
        ]))     
        interface.run()

    # def test_ship_setup_scenario_fails_first_try(self):
    #     io = TerminalInterfaceHelperMock()
    #     interface = UserInterface(io, Game())
    #     io.expect_print("Welcome to the game!")
    #     io.expect_print("Set up your ships first.")
    #     io.expect_print("You have these ships remaining: 2, 3, 3, 4, 5")
    #     io.expect_print("Which do you wish to place?")
    #     io.provide("5")
    #     io.expect_print("Vertical or horizontal? [vh]")
    #     io.provide("v")
    #     io.expect_print("Which row?")
    #     io.provide("10")
    #     io.expect_print("Which column?")
    #     io.provide("1")
    #     io.expect_print("INVALID!")
    #     # Second Try
    #     io.expect_print("You have these ships remaining: 2, 3, 3, 4, 5")
    #     io.expect_print("Which do you wish to place?")
    #     io.provide("2")
    #     io.expect_print("Vertical or horizontal? [vh]")
    #     io.provide("v")
    #     io.expect_print("Which row?")
    #     io.provide("3")
    #     io.expect_print("Which column?")
    #     io.provide("2")
    #     io.expect_print("OK.")
    #     io.expect_print("This is your board now:")
    #     io.expect_print("\n".join([
    #         "..........",
    #         "..........",
    #         ".S........",
    #         ".S........",
    #         "..........",
    #         "..........",
    #         "..........",
    #         "..........",
    #         "..........",
    #         ".........."
    #     ]))
    #     io.expect_print("Done, for now!")
    #     interface.run()
