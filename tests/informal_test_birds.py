from lib.bird import Bird
from lib.hummingbird import Hummingbird
from lib.penguin import Penguin

if __name__ == '__main__':
    a_bird = Bird()

    assert a_bird.fly()
    assert not a_bird.walk()

    a_hummingbird = Hummingbird()

    assert a_hummingbird.fly()
    assert not a_hummingbird.walk()

    a_penguin = Penguin()

    assert not a_penguin.fly()
    assert a_penguin.walk()


