import pytest

from minimuh.core import car_say, cow_say, martin_say, robot_say


@pytest.mark.parametrize("text, say_function, expected_text", [
    ("hello", car_say, "im car: hello"),
    ("moo", cow_say, "im cow: moo"),
    ("umami", martin_say, "im martin: umami"),
])
def test_say_functions(text, say_function, expected_text):
    assert say_function(text) == expected_text


@pytest.mark.parametrize("robot_id", [1, 33, 1000])
def test_robot_say(robot_id):
    assert (robot_say(robot_id, "i destroy earth") == f"im robot_{robot_id}: i destroy earth")
