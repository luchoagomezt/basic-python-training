from lib.penguin import Penguin


def test_pinguin_walks():
    a_penguin = Penguin()
    assert a_penguin.walk()


def test_penguin_does_not_fly():
    a_penguin = Penguin()
    assert not a_penguin.fly()

