from minimuh.text_wrappers import wrap_into_braces


def test_wraps_into_braces():
    assert wrap_into_braces("good day") == "[good day]"