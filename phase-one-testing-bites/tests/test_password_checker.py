import pytest
from lib.password_checker import *

def test_password_checker_long_enough():
    checker = PasswordChecker()
    result = checker.check("longEnough")
    assert result == True

def test_password_checker_empty():
    checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        checker.check("")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."

def test_password_checker_too_short():
    checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        checker.check("short")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."