from demoapp.library import bar

def test_bar_value():
    assert bar() == "demoapp.library is greeting you!"
