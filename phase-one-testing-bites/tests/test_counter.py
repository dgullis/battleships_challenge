from lib.counter import *

def test_counter_add_none():
    counter = Counter()
    result = counter.report()
    assert result == "Counted to 0 so far."

def test_counter_add_twice():
    counter = Counter()
    counter.add(5)
    counter.add(15)
    result = counter.report()
    assert result == "Counted to 20 so far."

def test_counter_add_five_times():
    counter = Counter()
    counter.add(5)
    counter.add(15)
    counter.add(7)
    counter.add(3)
    counter.add(10)
    result = counter.report()
    assert result == "Counted to 40 so far."