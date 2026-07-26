from bank import value

def test_value1():
    assert value("Hello, World!") == 0

def test_value2():
    assert value("Hey, there!") == 20

def test_value3():
    assert value("What's up?") == 100

if __name__ == "__main__":
    test_value1()
    test_value2()
    test_value3()