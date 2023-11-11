from lib.string_builder import *

def test_string_builder_add_and_output():
    stringBuilder = StringBuilder()
    stringBuilder.add("Hello")
    stringBuilder.add(" John")
    result = stringBuilder.output()
    assert result == "Hello John"

def test_string_builder_size():
    stringBuilder = StringBuilder()
    stringBuilder.add("Hello")
    stringBuilder.add(" John")
    result = stringBuilder.size()
    assert result == 10