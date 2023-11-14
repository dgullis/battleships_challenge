import pytest
from lib.grammar_stats import *

def test_check_sentence_grammar_without_capital():
    checker = GrammarStats()
    result = checker.check('this will not pass!')
    assert result == False

def test_check_sentence_grammar_passes_with_question():
    checker = GrammarStats()
    result = checker.check('Will this pass?')
    assert result == True 

def test_check_sentence_fails_without_ending_punctuation():
    checker = GrammarStats()
    result = checker.check('This will not pass')
    assert result == False 

def test_percentage_good_all_passed():
    checker = GrammarStats()
    checker.check("This is a sentence.")
    checker.check("This is a sentence.")
    result = checker.percentage_good()
    assert result == 100

def test_percentage_good_half_passed():
    checker = GrammarStats()
    checker.check("This is a sentence.")
    checker.check("This is a sentence")
    result = checker.percentage_good()
    assert result == 50

def test_percentage_good_half_passed():
    checker = GrammarStats()
    checker.check("This is a sentence.")
    checker.check("This is a sentence.")
    checker.check("This is a sentence.")
    checker.check("This is a sentence")
    result = checker.percentage_good()
    assert result == 75