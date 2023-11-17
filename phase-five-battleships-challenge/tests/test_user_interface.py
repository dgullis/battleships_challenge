from lib.user_interface import *
from tests.terminal_interface_helper_mock import TerminalInterfaceHelperMock
from unittest.mock import Mock

"""
test incorrect ship choice
"""
def test_ship_setup_invalid_ship_size_on_first_try():
    io = TerminalInterfaceHelperMock()
    interface = UserInterface(io, Mock())
    io.expect_print("Welcome to the game!")
    io.expect_print("Set up your ships first.")
    io.expect_print("You have these ships remaining: 2, 3, 3, 4, 5")
    io.expect_print("Which do you wish to place?")
    io.provide("1")
    io.expect_print("invalid ship, choose again...")
    io.provide("2")
    io.expect_print("Vertical or horizontal? [vh]")
    io.provide("v")
    io.expect_print("Which row?")
    io.provide("3")
    io.expect_print("Which column?")
    io.provide("2")
    io.expect_print("OK.")
    io.expect_print("This is your board now:")
    

"""
test incorrect orientation choice
"""

def test_ship_setup_invalid_orientation():
    io = TerminalInterfaceHelperMock()
    interface = UserInterface(io, Mock())
    io.expect_print("Welcome to the game!")
    io.expect_print("Set up your ships first.")
    io.expect_print("You have these ships remaining: 2, 3, 3, 4, 5")
    io.expect_print("Which do you wish to place?")
    io.provide("2")
    io.expect_print("Vertical or horizontal? [vh]")
    io.provide("vertical")
    io.expect_print("invalid orientation, choose again...")
    io.provide("v")
    io.expect_print("Which row?")
    io.provide("3")
    io.expect_print("Which column?")
    io.provide("2")
    io.expect_print("OK.")
    io.expect_print("This is your board now:")


"""
test incorrect row choice
"""

def test_ship_setup_invalid_row():
    io = TerminalInterfaceHelperMock()
    interface = UserInterface(io, Mock())
    io.expect_print("Welcome to the game!")
    io.expect_print("Set up your ships first.")
    io.expect_print("You have these ships remaining: 2, 3, 3, 4, 5")
    io.expect_print("Which do you wish to place?")
    io.provide("2")
    io.expect_print("Vertical or horizontal? [vh]")
    io.provide("v")
    io.expect_print("Which row?")
    io.provide("11")
    io.expect_print("out of bounds, choose again...")
    io.expect_print("Which row?")
    io.provide("3")
    io.expect_print("Which column?")
    io.provide("2")
    io.expect_print("OK.")
    io.expect_print("This is your board now:")

"""
test incorrect col choice
"""

def test_ship_setup_invalid_column():
    io = TerminalInterfaceHelperMock()
    interface = UserInterface(io, Mock())
    io.expect_print("Welcome to the game!")
    io.expect_print("Set up your ships first.")
    io.expect_print("You have these ships remaining: 2, 3, 3, 4, 5")
    io.expect_print("Which do you wish to place?")
    io.provide("2")
    io.expect_print("Vertical or horizontal? [vh]")
    io.provide("v")
    io.expect_print("Which row?")
    io.provide("3")
    io.expect_print("Which column?")
    io.provide("-1")
    io.expect_print("Out of bounds, choose again...")
    io.expect_print("Which column")
    io.provide("2")
    io.expect_print("OK.")
    io.expect_print("This is your board now:")
    

"""
test invalid row choice given ship length and co-ordinates
"""

def test_ship_setup_invalid_ship_collision():
    io = TerminalInterfaceHelperMock()
    interface = UserInterface(io, Mock())
    io.expect_print("Welcome to the game!")
    io.expect_print("Set up your ships first.")
    io.expect_print("You have these ships remaining: 2, 3, 3, 4, 5")
    io.expect_print("Which do you wish to place?")
    io.provide("3")
    io.expect_print("Vertical or horizontal? [vh]")
    io.provide("v")
    io.expect_print("Which row?")
    io.provide("9")
    io.expect_print("Which column?")
    io.provide("1")
    io.expect_print("Out of bounds, choose again...")
    io.expect_print("Which row?")
    io.provide("3")
    io.expect_print("Which column?")
    io.provide("2")
    io.expect_print("OK.")
    io.expect_print("This is your board now:")

# def test_ship_setup_scenario(self):
#     io = TerminalInterfaceHelperMock()
#     interface = UserInterface(io, Mock())
#     io.expect_print("Welcome to the game!")
#     io.expect_print("Set up your ships first.")
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