from minimuh.core import car_say


def test_car_say():
    assert car_say("hello") == "im car: hello"