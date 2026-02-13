from hello import more_hello, more_bye


def test_more_hello():
    assert "hello" == more_hello()


def test_more_bye():
    assert "bye" == more_bye()
