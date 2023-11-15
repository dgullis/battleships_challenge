from unittest.mock import Mock
from lib.time_error import *

def test_calls_to_api_to_get_server_time():
    requester_mock = Mock(name="requester")
    response_mock = Mock(name="response")
    time_mock = Mock(name="time")

    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {"unixtime":1700080561}
    time_mock.time.return_value = 1700080566

    check_time_error = TimeError(requester_mock, time_mock)
    result = check_time_error.error()
    assert result == -5