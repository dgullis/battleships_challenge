from lib.report_length import *

def test_report_length_empty():
    result = report_length("")
    assert result == "This string was 0 characters long."

def test_report_length_four():
    result = report_length("four")
    assert result == "This string was 4 characters long."

def test_report_length_empty():
    result = report_length("123456789abcdefghijk")
    assert result == "This string was 20 characters long."