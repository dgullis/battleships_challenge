from lib.check_codeword import *

def test_check_codeword_horse():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_check_codeword_house():
    result = check_codeword("house")
    assert result == "Close, but nope."

def test_check_codeword_password():
    result = check_codeword("password")
    assert result == "WRONG!"