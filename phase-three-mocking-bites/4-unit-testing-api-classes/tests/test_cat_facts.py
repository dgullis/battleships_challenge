from unittest.mock import Mock
from lib.cat_facts import *

def test_calls_to_api_to_get_cat_fact():
    request_mock = Mock()
    response_mock = Mock()

    request_mock.get.return_value = response_mock
    response_mock.json.return_value = {"fact":"Cats purr at the same frequency as an idling diesel engine, about 26 cycles per second.", "length":87}

    cat_fact = CatFacts(request_mock)
    result = cat_fact.provide()
    assert result == "Cat fact: Cats purr at the same frequency as an idling diesel engine, about 26 cycles per second."

